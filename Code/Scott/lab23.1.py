"""
Name:           Scott Tran
Date            6/24/2019
Assignment:     Build a program to manage a list of contacts in a CSV file. Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user.

"""
import csv
from pprint import pprint


with open('contacts.csv', mode='r') as file:
    reader = csv.reader(file)
    # next(reader) # skip header
    dict_contacts = {}
    for row in reader:
        dict_contacts[row[0]]=row[1:]

pprint(dict_contacts)