import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        return Person(self.name, self.email, self.phone, self.favorite)
             


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        result.contacts = copy.copy(self.contacts)
        return result
        
        

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for key, value in self.__dict__.items():
            setattr(result, key, copy.deepcopy(value, memo))
        return result
        
def copy_class_contacts(contacts: Contacts) -> Contacts:
    return copy.deepcopy(contacts)        
# Приклад створення екземплярів класу Person
contact1 = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

contact2 = Person(
    "Chaim Lewis",
    "dui.in@egetlacus.ca",
    "(294) 840-6685",
    False,
)

# Створення списку контактів
contacts = [contact1, contact2]

# Приклад створення екземпляра класу Contacts
persons = Contacts("user_class.dat", contacts)

# Створення поверхневої копії екземпляра класу Person
copy_person = copy.copy(contact1)
print(copy_person == contact1)  # True
print(copy_person.name == contact1.name)  # True

# Створення глибокої копії екземпляра класу Contacts
new_persons = copy_class_contacts(persons)

# Зміна імені в копії
new_persons.contacts[0].name = "Another name"

# Перевірка
print(persons.contacts[0].name)  # Allen Raymond
print(new_persons.contacts[0].name)  # Another name   
        
        