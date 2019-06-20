'''
# parse_csv.py

Parses CSV file of contacts into dictionary
'''

with open('contacts.csv') as f:
    contents = f.read() # store string of file contents

rows = contents.split('\n') # get rows by splitting lines
# print(contents)
# print(rows)
rows = [contact.split(',') for contact in rows] # split each row by commas
# print(rows)

# contacts = [] # start off with empty contacts list
contacts = {} # start off with blank contacts dict
headings = rows[0] # the first row is special
                   # it's the headings (i.e. keys) of your contacts dict

for i in range(1, len(rows)): # skip the first row since it's your headings
    contact = dict(zip(headings, rows[i])) # create a contact dict
                                           # combining keys from headings
                                           # and values from the row
    # contacts.append(contact)
    contacts[contact['name']] = contact # add contact to your contacts
                                        # key is name, val is contact dict

print('Here are your contacts:', contacts.keys())

# query your contacts list by name and field
name = input('Enter contact name: ')
print('Possible fields:', headings)
field = input('Enter field: ')
print(contacts[name][field])
