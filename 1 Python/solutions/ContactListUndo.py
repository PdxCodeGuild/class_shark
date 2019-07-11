'''
ContactList.py

Open/modify/save contact list as csv file

- Parses csv of self.contacts into a python dictionary
- Uses REPL user interface to allow CRUD (create, read, update, delete) methods on contact list
- Saves contact list dictionary back into csv file.
'''
from data_structures.Stack import Stack

class InvalidContactListException(Exception):
    def __init__(self):
        super().__init__()
        self.msg = 'Not a valid ContactList object'

    def __repr__(self):
        return self.msg


class ContactList:
    def __init__(self, filename=None, headers=None):
        if filename:
            self.read_csv(filename)
        else:
            self.contacts = {}
            self.headers = headers
        self.state = Stack()
        self.redo_stack = Stack()
        self.state.push(self.contacts.copy())

    def __str__(self):
        str_repr = '-'*60 + '\n'
        for contact in self.contacts:
            str_repr += self.contact_to_str(contact) + '-'*60 + '\n'
        str_repr += 'State: ' + str(self.state) + '\n'
        str_repr += 'Redo: ' + str(self.redo_stack) + '\n'
        return str_repr

    def __eq__(self, contact_list):
        if type(contact_list) is ContactList:
            return self.contacts == contact_list.contacts
        return False

    def __len__(self):
        return len(self.contacts)

    def __contains__(self, element):
        return element in self.contacts

    def __getitem__(self, key):
        return self.contacts[key]

    def __add__(self, element):
        if type(element) is ContactList or type(element) is dict:
            temp = self.contacts.copy()
            if type(element) is ContactList:
                temp.update(element.contacts)
            elif type(element) is dict:
                temp = ContactList(headers=self.headers)
                temp.contacts = self.contacts
                temp.create(element)
            return temp
        else:
            raise InvalidContactListException

    def __iadd__(self, element):
        if type(element) is ContactList:
            self.contacts.update(element.contacts)
            return self
        elif type(element) is dict:
            self.create(element)
            return self
        else:
            raise InvalidContactListException

    def __clear_redo(self):
        if self.redo_stack:
            self.redo_stack = Stack()

    def read_csv(self, filename):
        '''
        :filename: str of csv filepath

        parses csv and returns dictionary of self.contacts
        '''
        with open(filename) as f:
            contents = f.read()

        lines = contents.split('\n')
        self.headers = lines[0].split(',')
        self.contacts = {}
        for i in range(1, len(lines)):
            row = lines[i].split(',')
            contact = dict(zip(self.headers, row))
            self.contacts[contact['name']] = contact

    def write_csv(self, filename):
        '''
        :filename: str of csv filepath

        converts contact list to csv and writes to file
        '''
        headers = ','.join(self.headers)
        lines = [headers]
        for name in self.contacts:
            row = ','.join(self.contacts[name].values())
            lines.append(row)
        lines = '\n'.join(lines)

        with open(filename, 'w') as f:
            f.write(lines)

    def create(self, contact):
        '''
        :contact: dict representing individual contact

        creates contact and adds to contact list
        '''
        self.contacts[contact['name']] = contact
        self.state.push(self.contacts.copy())
        self.__clear_redo()
        return f"Added {contact['name']}"

    def read(self, name):
        '''
        :name: str of contact's name

        returns contact if name found in contact list
        '''
        contact = self.contacts.get(name)
        if contact:
            return self.contact_to_str(name)
        else:
            return f'{name} not found'

    def update(self, name, details):
        '''
        :name: str of contact's name
        :details: dict of details to update contact with

        updates contact if name found in contact list
        '''
        if name in self.contacts:
            self.contacts[name].update(details)
            self.state.push(self.contacts.copy())   
            self.__clear_redo()
        return self.read(name)

    def delete(self, name):
        '''
        :name: str of contact's name

        deletes contact if name found in contact list
        '''
        if name in self.contacts:
            del self.contacts[name]
            self.state.push(self.contacts.copy())  
            self.__clear_redo()              
            return f'Deleted {name}'
        else:
            return f'{name} not found'

    def contact_to_str(self, name):
        str_repr = ''
        for key, val in self.contacts[name].items():
            str_repr += f'{key}: {val}' + '\n'
        return str_repr

    def undo(self):
        '''
        Undos last operation
        Pops last state onto redo stack
        '''
        if len(self.state) > 1:
            self.redo_stack.push(self.state.pop())
            self.contacts = self.state.peek().copy()

    def redo(self):
        '''
        Redos last operation
        Pops last state onto redo stack
        '''        
        if redo_stack:
            self.state.push(self.redo_stack.pop())
            self.contacts = self.state.peek().copy()


def repl():
    '''
    REPL user interface
    '''
    contact_list = ContactList('contact_list.csv')
    commands = [
        'c', 'create',
        'r', 'read',
        'u', 'update',
        'd', 'delete',
        'h', 'help',
        'l', 'list',
        'x', 'exit',
        'un', 'undo', 
        're', 'redo'
    ]
    help_msg = '''
    (c)reate, 
    (r)ead, 
    (u)pdate, 
    (d)elete, 
    (l)ist, 
    (un)do, 
    (re)do, or 
    e(x)it
    '''
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
            for key in contact_list.headers:
                val = input(f'{key}: ')
                contact[key] = val
            print(contact_list.create(contact))
        elif cmd in ['r', 'read', 'u', 'update', 'd', 'delete']:
            name = input('Name: ')
            if cmd.startswith('r'):
                print(contact_list.read(name))
            elif cmd.startswith('u'):
                print('Enter updated values, or leave blank for original.')            
                details = {}
                for key in contact_list.headers:
                    val = input(f'{key}: ')
                    if val:
                        details[key] = val
                print(contact_list.update(name, details))                        
            elif cmd.startswith('d'):
                print(contact_list.delete(name))
        elif cmd.startswith('h'):
            print(help_msg)
        elif cmd.startswith('l'):
            print(contact_list)
        elif cmd.startswith('un'):
            contact_list.undo()            
        elif cmd.startswith('re'):
            contact_list.redo()            
        else:
            loop = False
            print('Saving to file...')
            contact_list.write_csv('contact_list.csv')


if __name__ == '__main__':
    repl()