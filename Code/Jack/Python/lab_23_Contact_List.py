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
        rows = [item.split(',') for item in lines]
        self.headings = rows[0]
        for i in range(1, len(rows)):
            contact = dict(zip(self.headings, rows[i]))
            # self.contacts[rows[0]] = [rows[1], rows[2]]
            self.contacts[contact['name']] = contact

    def view_contacts(self):
        '''
        shows current contact names
        '''
        print('Your contacts are:')
        for i in self.contacts:
            print(i)

    def get_contact(self, con):
        '''
        returns contact as a dict, if contact is not found, returns empty
        '''
        if con in self.contacts:
            # print(self.contacts[con])
            return self.contacts[con]
        else:
            print('contact not found:')
            return {'name': '', 'fav_food': '', 'fav_color': ''}

    def update_contacts(self, name, fav_food, fav_color):
        '''
        updates contacts csv file
        '''

        self.contacts.update({name: dict(zip(self.headings,
                                             [name, fav_food, fav_color]))})

    def update_file(self):
        lines = 'name, fav_food, fav_color\n'
        for item in self.contacts:
            lines += (self.contacts[item]['name'] + ', ' +
                      self.contacts[item]['fav_food'] + ', ' +
                      self.contacts[item]['fav_color'] + '\n')
        with open(self.source_file, 'w') as file:
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
crd.update_contacts(n, ff, fc)
crd.view_contacts()
crd.remove_contact('Kipper')
crd.view_contacts()
# cur_con = crd.get_contact('Kip')
crd.update_file()
# crd.remove_contact('Kip')
# crd.view_contacts()
# print(crd.contacts.items())

def main():
    pass


main()
