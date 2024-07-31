"""
import pickle

def write_contacts_to_file(filename, contacts):
    
    Функція для запису списку контактів у файл.
    
    :param filename: Ім'я файлу для запису.
    :param contacts: Список контактів для запису.

    with open(filename, "wb") as file:
        pickle.dump(contacts, file)

def read_contacts_from_file(filename):
     Функція для читання списку контактів з файлу.
    
    :param filename: Ім'я файлу для читання.
    :return: Повертає список контактів.
  
    with open(filename, "rb") as file:
        return pickle.load(file)
"""

import pickle

def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as file:
        pickle.dump(contacts, file)

def read_contacts_from_file(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)