#LAB 23 CONTACT LIST
#OPEN A CSV FILE
#CONVERT LINES OF TEXT TO LIST OF DICTIONARIES
#Header represents the Keys
#Text in other lines represent the values

def read_csv(file):
    contact_list = []
    with open('contacts.csv','r') as file:
        lines = file.read().split('\n')
        headers = lines[0].split(',')
        contact = dict(zip(headers, lines))
        #print(lines)
        #print(headers)

    for i in range(1, len(lines)):
        row = lines[i].split(',')
        contact = dict(zip(headers,row))
        contact_list.append(contact)
    #return contact_list
    return (contact_list, headers)

#contact_list = []
#for row in contact_list:
#    contact_list.append(row.replace(' ','').split(','))
#    print (contact_list)

def write_csv(contact_list, headings, file):
    headings = ','.join(headings)
    lines = [headings]
    for name in contact_list:
        row = ','.join(name.values())
        lines.append(row)
    lines = '\n'.join(lines)

    with open(file, 'w') as file:
        file.write(lines)

def create(contact_list, contact):

    contact_list[contact['name']] = contact
    return f"Added {contact['name']}"

def read(contact_list, name):
    return contact_list.get(name, f'{name} not found')

#def update(contact_list, name, details):
