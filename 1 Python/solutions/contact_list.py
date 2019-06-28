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
    pass


def write_csv(contacts, filename):
    '''
    :contacts: dict of contact list
    :filename: str of csv filepath

    converts contact list to csv and writes to file
    '''
    pass


def create(contacts, contact):
    '''
    :contacts: dict of contact list
    :contact: dict representing individual contact

    creates contact and adds to contact list
    '''
    pass


def read(contacts, name):
    '''
    :contacts: dict of contact list
    :name: str of contact's name

    returns contact if name found in contact list
    '''
    pass


def update(contacts, name, details):
    '''
    :contacts: dict of contact list
    :name: str of contact's name
    :details: dict of details to update contact with

    updates contact if name found in contact list
    '''
    pass


def delete(contacts, name):
    '''
    :contacts: dict of contact list
    :name: str of contact's name

    deletes contact if name found in contact list
    '''
    pass    


def repl():
    '''
    REPL user interface
    '''
    pass


if __name__ == '__main__':
    repl()