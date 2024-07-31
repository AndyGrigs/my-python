import json


def write_contacts_to_file(filename, contacts):

    
    data = {"contacts": contacts}
    
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    
        


def read_contacts_from_file(filename):

    with open(filename, "r") as file:
        data = json.load(file)
        return data["contacts"]
    
c =   {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

write_contacts_to_file("c.json", c)

r = read_contacts_from_file("c.json")

print(r)