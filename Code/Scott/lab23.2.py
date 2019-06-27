"""
Name:           Scott Tran
Date            6/24/2019
Assignment:     From your dictionary build on a CSV, Implement a CRUD REPL. 

"""
import csv
from pprint import pprint


def append_dict(dict_x):
    first_name = input("What is your first name: ") 
    fav_fruit = input("What is your favorite fruit: ")
    fav_color = input("What is your favorit color: ",)

    dict_x.update([(first_name, [fav_fruit, fav_color])])
    return dict_x


def find_name(dict_x):
    while True:
        try:
            name_finder = input("Who would you like to find? ")
            return(f"{name_finder}'s favorite fruit is {dict_contacts[name_finder][0]} and favorite color is {dict_contacts[name_finder][1]}.")
        except KeyError:
            print("No one with the name exists in the file. Please try again ...") 


def update_name(dict_x):
    while True:
        try:
            name_finder = input("Whose record would you like to update? ")
            update_fruit = input("what is their new favorit fruit? ")
            update_color = input("What is their new favorite color? ")
            dict_x[name_finder][0] = update_fruit 
            dict_x[name_finder][1] = update_color
            return dict_x
        except KeyError:
            print("No one with the name exists in the file. Please try again ...") 


def delete_name(dict_x):
    while True:
        try:
            name_finder = input("Whose record would you like to delete? ")
            del dict_x[name_finder]
            return dict_x
        except KeyError:
            print("No one with the name exists in the file. Please try again ...") 


with open('contacts.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader) # skip header
    dict_contacts = {}
    for row in reader:
        dict_contacts[row[0]]=row[1:]


print("---Old File---" + "-"*50)
pprint(dict_contacts)
print("\n---Appended File---" + "-"*45)

pprint(append_dict(dict_contacts))

print("\n---Retreive File---" + "-"*45)

print(find_name(dict_contacts))

print("\n---Updated File---" + "-"*46)

pprint(update_name(dict_contacts))

print("\n---Delete File---" + "-"*47)

pprint(delete_name(dict_contacts))
