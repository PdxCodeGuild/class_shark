'''
contact_list.py

Open/modify/save contact list as csv file

- Parses csv of contacts into a python dictionary
- Uses REPL user interface to allow CRUD (create, read, update, delete) methods on contact list
- Saves contact list dictionary back into csv file.
'''

def read_csv(filename):
    '''
    :filename: str of csv filepath

    parses csv and returns dictionary of contacts
    '''
    with open(filename) as f:
        contents = f.read()

    lines = contents.split('\n')
    headers = lines[0].split(',')
    contacts = {}
    for i in range(1, len(lines)):
        row = lines[i].split(',')
        contact = dict(zip(headers, row))
        contacts[contact['name']] = contact
    return contacts


def write_csv(contacts, headings, filename):
    '''
    :contacts: dict of contact list
    :filename: str of csv filepath

    converts contact list to csv and writes to file
    '''
    headings = ','.join(headings)
    lines = [headings]
    for name in contacts:
        row = ','.join(contacts[name].values())
        lines.append(row)
    lines = '\n'.join(lines)

    with open(filename, 'w') as f:
        f.write(lines)


def create(contacts, contact):
    '''
    :contacts: dict of contact list
    :contact: dict representing individual contact

    creates contact and adds to contact list
    '''
    contacts[contact['name']] = contact
    return f"Added {contact['name']}"


def read(contacts, name):
    '''
    :contacts: dict of contact list
    :name: str of contact's name

    returns contact if name found in contact list
    '''
    return contacts.get(name, f'{name} not found')


def update(contacts, name, details):
    '''
    :contacts: dict of contact list
    :name: str of contact's name
    :details: dict of details to update contact with

    updates contact if name found in contact list
    '''
    if name in contacts:
        contacts[name].update(details)
    return read(contacts, name)


def delete(contacts, name):
    '''
    :contacts: dict of contact list
    :name: str of contact's name

    deletes contact if name found in contact list
    '''
    if name in contacts:
        del contacts[name]
        return f'Deleted {name}'
    else:
        return f'{name} not found'


def print_contact(contacts, name):
    for key, val in contacts[name].items():
        print(f'{key}: {val}')


def print_all(contacts):
    print('-'*60)
    for contact in contacts:
        print_contact(contacts, contact)
        print('-'*60)


def repl():
    '''
    REPL user interface
    '''
    headers = ['name', 'age', 'job']
    contact_list = read_csv('contact_list.csv')
    commands = [
        'c', 'create',
        'r', 'read',
        'u', 'update',
        'd', 'delete',
        'h', 'help',
        'l', 'list',
        'x', 'exit'
    ]
    help_msg = '(c)reate, (r)ead, (u)pdate, (d)elete, (l)ist, or e(x)it'
    loop = True
    print('Welcome to your contact list')
    print(help_msg)
    while loop:
        while True:
            cmd = input('>').strip().lower()
            if cmd in commands:
                break
            print(help_msg)

        if cmd.startswith('c'):
            contact = {}
            for key in headers:
                val = input(f'{key}: ')
                contact[key] = val
            print(create(contact_list, contact))
        elif cmd in ['r', 'read', 'u', 'update', 'd', 'delete']:
            name = input('Name: ')
            if cmd.startswith('r'):
                read(contact_list, name)
                print_contact(contact_list, name)
            elif cmd.startswith('u'):
                print('Enter updated values, or leave blank for original.')            
                details = {}
                for key in headers:
                    val = input(f'{key}: ')
                    if val:
                        details[key] = val
                print(update(contact_list, name, details))                        
            elif cmd.startswith('d'):
                print(delete(contact_list, name))
        elif cmd.startswith('h'):
            print(help_msg)
        elif cmd.startswith('l'):
            print_all(contact_list)
        else:
            loop = False
            print('Saving to file...')
            write_csv(contact_list, headers, 'contact_list.csv')


if __name__ == '__main__':
    repl()