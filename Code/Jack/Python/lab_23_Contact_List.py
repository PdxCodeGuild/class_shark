from termcolor import colored as c


class crud_repl():
    '''
    class for viewing and modifying contact information on a csv file
    '''

    contacts = {}
    headings = []
    source_file = './Resources/contacts.csv'

    def __init__(self):
        self.pull_contacts()

    def pull_contacts(self):
        '''
        pulls contacts from csv file and assigns them to a nested dict.
        Only needs to be called once during instantiation
        To change the file it pulls from change the self.source_file value
        '''
        with open(self.source_file, 'r') as file:
            lines = file.read().split('\n')

        for i in range(len(lines)):
            lines[i] = lines[i].replace(' ', '')
        lines.pop()
        self.headings = lines[0].split(',')
        for i in range(1, len(lines)):
            row = lines[i].split(',')
            contact = dict(zip(self.headings, row))
            self.contacts[contact['name']] = contact

        # # This one has two for loops the above has only one:
        # rows = [item.split(',') for item in lines]
        # self.headings = rows[0]
        # for i in range(1, len(rows)):
        #     contact = dict(zip(self.headings, rows[i]))
        #     # self.contacts[rows[0]] = [rows[1], rows[2]]
        #     self.contacts[contact['name']] = contact

    def view_contacts(self):
        '''
        shows current contact names
        '''
        print('Your contacts are:')
        for i in self.contacts:
            print(i)

    def get_contact(self, name):
        '''
        returns contact as a dict, if contact is not found, returns empty
        '''
        return self.contacts.get(name, 'contact not found:')

    # def update_contacts_v1(self, name, fav_food, fav_color):
    #     '''
    #     creates new contact, if 'updating' be sure to 'remove' old contact
    #     '''
    #     self.contacts.update({name: dict(zip(self.headings,
    #                                          [name, fav_food, fav_color]))})

    def update_contacts(self, name, details):
        self.contacts[name].update(details)

    def add_contact(self, contact):
        '''
        creates new contact, if 'updating' be sure to 'remove' old contact
        '''
        self.contacts[contact['name']] = contact

    def update_file(self):
        lines = [','.join(self.headings)]
        # for item in self.contacts:
        #     lines += (self.contacts[item]['name'] + ', ' +
        #               self.contacts[item]['fav_food'] + ', ' +
        #               self.contacts[item]['fav_color'] + '\n')
        for item in self.contacts:
            lines.append(','.join(self.contacts[item].values()))
        lines = '\n'.join(lines)
        with open('./Resources/contacts2.csv', 'w') as file:
            file.write(lines)

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print('record not found\n')


crd = crud_repl()
crd.pull_contacts()
crd.view_contacts()
n = 'Kipper'
ff = 'burgers'
fc = 'forest green'
# crd.update_contacts(n,{'name':n, 'fav_food':ff, 'fav_color':fc})
crd.add_contact({'name': n, 'fav_food': ff, 'fav_color': fc})
crd.view_contacts()
# crd.remove_contact('Kipper')
# crd.view_contacts()
# cur_con = crd.get_contact('Kip')
crd.update_file()
# crd.remove_contact('Kip')
# crd.view_contacts()
# print(crd.contacts.items())


def create(object):
    while True:
        name = input('Name: ').strip().lower()
        food = input('Favorite food: ').strip().lower()
        color = input('Favorite color: ').strip().lower()
        print(name, food, color)
        ch = input('is this correct? y/n\n').strip().lower()
        if ch.startswith('y'):
            object.update_contacts(name, food, color)
            break


def retrieve(object):
    object.view_contacts()
    name = input('Name: ').strip().lower()
    print(object.get_contact(name))


def update_con(object):
    '''
    updates any field within contacts.
    will update field, create new contact, delete old contact
    '''
    while True:
        object.view_contacts()
        name = input('Name: ').strip().lower()
        cur_con = object.get_contact(name)
        prev_name = name
        food = cur_con['fav_food']
        color = cur_con['fav_color']
        print(cur_con[name]['name'], cur_con['fav_food'], cur_con['fav_color'])
        print('what would you like to update?\n',
              c('N', 'red'), 'ame\n',
              c('F', 'red'), 'ood\n',
              c('C', 'red'), 'olor')
        ch = input().strip().lower()
        if ch.startswith('n'):
            name = input('New name: ').strip().lower()
        elif ch.startswith('f'):
            food = input('New favorite food: ').strip().lower()
        elif ch.startswith('c'):
            color = input('New favorite color: ').strip().lower()
        else:
            print('incorrect input')
    cur_con.remove_contact(prev_name)
    object.update_contacts(name, food, color)

    food = input('New favorite food: ').strip().lower()
    color = input('New favorite color: ').strip().lower()
    print(name, food, color)
    ch = input('is this correct? y/n\n').strip().lower()
    if ch.startswith('y'):
        object.update_contacts(name, food, color)
        # break


def del_con(object):
    pass


def main():
    # exit = False
    # while not exit:
    #     con = crud_repl()
    #     con.view_contacts()
    #     print(c('C', 'red'), 'reate, ',
    #           c('R', 'red'), 'etrieve, ',
    #           c('U', 'red'), 'pdate, ',
    #           c('D', 'red'), 'elete, or ',
    #           c('E', 'red'), 'xit: ')
    #     user_ch = input().strip().lower()
    #     if user_ch.startswith('e') or user_ch == 'x':
    #         con.update_file()
    #         exit = True
    #     elif user_ch.startswith('c'):
    #         create(con)
    #     elif user_ch.startswith('r'):
    #         retrieve(con)
    #     elif user_ch.startswith('u'):
    #         update_con(con)
    #     elif user_ch.startswith('d'):
    #         del_con(con)
    #     else:
    #         print('incorrect input')

    con = crud_repl()
    con.view_contacts()
    commands = [
        'c', 'create',
        'r', 'retrieve',
        'u', 'update',
        'd', 'delete',
        'h', 'help',
        'l', 'list',
        'x', 'exit'
    ]
    exit = False
    while not exit:
        while True:
            cmd = input('(c)reate, (r)etrieve, (u)pdate, (d)elete, (l)ist, or e(x)it: ').lower().strip()
            if cmd in commands:
                break
        if cmd.startswith('e') or cmd == 'x':
            con.update_file()
            exit = True
        elif cmd.startswith('c'):
            create(con)
        elif cmd.startswith('r'):
            retrieve(con)
        elif cmd.startswith('u'):
            update_con(con)
        elif cmd.startswith('d'):
            del_con(con)

main()
