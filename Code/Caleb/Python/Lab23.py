# Lab 23: Contact List
# Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys, the text in the other lines represent the values.

# contacts = [{'name': 'George', 'favorite fruit':'avocado', 'favorite color': 'green'},{'name': 'Billy', 'favorite fruit':'strawberry', 'favorite color': 'red'},{'name': 'Simon', 'favorite fruit':'apple', 'favorite color': 'blue'}]

# with open('contacts.csv', 'w') as file:
#     for name, favorite fruit, favorite color in list(contacts.items()):
#         line = f'{name} {favoritefruit} {favoritecolor}\n'
#         file.write(line)


# Display Welcome Statement, Explain that we are opening a 'contacts.csv' file which was originally created by Caleb Mealey.
print('Welcome to Lab 23: Contact List. A program coded in python by Caleb Mealey.')
print('In this lab, we will open the \'contacts.csv\' file and allow the user to create a record, retrieve a record, update a record, or delete a record.')
print('')
print('In order to begin reading, manipulating, and more, we first recommend that you open the file and read it...')
print('We will open \'contacts.csv\' now.')


commands = ['c', 'create', 'l', 'list', 'r', 'retrieve', 'u', 'update', 'd', 'delete', 'x', 'e', 'exit']

class CRUD_REPL():
    '''
    class for implementation of a CRUD REPL, by viewing and modifying contact information on a .csv file, 'contacts.csv'.
    CRUD:
    - Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
    - Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
    - Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
    - Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
    REPL:
    - Read, Evaluate, Print Loop

    '''
    # Initialize header row list, which will hold the list of keys for the data columns on the top of the contacts.csv file.
    header_row_ls = []
    # Initialize the contacts dictionary
    contacts_dic = {}

    def __init__(self):
        '''
        Initialize the class, retrieve the contacts
        '''
        self.retrieve_all_contacts()
        self.main_menu()

    def retrieve_all_contacts(self):
        '''
        Retrieve the contacts and display just the names.
        '''
        with open('./assets/contacts.csv', 'r') as file:
            lines = file.read().split('\n')
            # print(lines)
            # lines.pop()
        self.header_row_ls = lines[0].split(',')
        for i in range(1, len(lines)):
            contact_data = lines[i].split(',')
            contact_row = dict(zip(self.header_row_ls, contact_data))
            self.contacts_dic[contact_row['name']] = contact_row
        print(self.contacts_dic)
        print('---' * 50)
        print('The contacts contained in \'contacts.csv\' are:')
        for y in self.contacts_dic:
            print(y)
        return(self.contacts_dic)


    def display_contact_names(self):
        '''
        Print the contacts contained in 'contacts.csv', printing each name an an individual line.
        '''
        print('---' * 50)
        print('The contacts contained in \'contacts.csv\' are:')
        for y in self.contacts_dic:
            print(y)
        pass

    def update(self):
        '''
        Function to update the actual 'contacts.csv' file, need to unpack the dictionary and then repack it into the existing file.
        '''
        with open('./assets/contacts.csv', 'w') as file:
            contacts_rows = []
            # print(self.header_row_ls)
            header_row = ','.join(self.header_row_ls)
            contacts_rows.append(header_row)
            # file.write(header_row)
            # file.write('/n')
            for i in self.contacts_dic:
                contact_row = ''
                # print(self.contacts_dic[i].items())
                # print(list(self.contacts_dic[i].values()))
                contact_row = ','.join(self.contacts_dic[i].values())
                contacts_rows.append(contact_row)
                # file.write(contact_row)
            print(f'We will now update \'contacts.csv\' with the following: {contacts_rows}')
            file.write('\n'.join(contacts_rows))
        pass

    def retrieve_one_contact(self, name):
        '''
        Function to retrieve one contact's specific details
        '''
        print(self.contacts_dic[name])
        for elem in self.contacts_dic[name]:
            print(f'{elem}: {self.contacts_dic[name][elem]}')
        return 'We will now return back to the main menu'

    def create_contact(self):
        '''
        Function to create a completely new contact. User will be prompted for the new contact's name, favorite food, and favorite color. This will be zipped up into the dictionary.
        '''
        print('We will now create a new contact in the file.')
        new_name = input('Enter the name of the contact: ')
        fav_food = input(f'Enter {new_name}\'s favorite food: ')
        fav_color = input(f'Enter {new_name}\'s favorite color: ')
        new_contact_data = [new_name, fav_food, fav_color]
        contact_row = dict(zip(self.header_row_ls, new_contact_data))
        self.contacts_dic[contact_row['name']] = contact_row
        print(self.contacts_dic)
        print(f'The contact, {new_name}, was added to \'contacts.csv\'')
        pass

    def update_contact(self, con_name):
        '''
        Function to update a specific contact's information
        '''
        for elem in self.contacts_dic[con_name]:
            print(f'{elem}: {self.contacts_dic[con_name][elem]}')
        new_fav_food = input(f'Enter {con_name}\'s updated favorite food: ')
        new_fav_color = input(f'Enter {con_name}\'s updated favorite color: ')
        updated_contact_data = [con_name, new_fav_food, new_fav_color]
        contact_row = dict(zip(self.header_row_ls, updated_contact_data))
        self.contacts_dic[contact_row['name']] = contact_row
        print(self.contacts_dic)
        print(f'The contact, {con_name}, was added to \'contacts.csv\'')
        pass

    def delete_contact(self, del_name):
        '''
        Function to call to delete a specific contact's entire name.
        '''
        del[self.contacts_dic[del_name]]
        print(f'The contact {del_name} has been deleted.')
        pass

    def main_menu(self):
        '''
        Main Menu Logic & Display Instructions
        '''
        print('---' * 50)
        print('\'contacts.csv\' is currently opened. What would you like to do?')
        print('You can (c)reate, (l)ist, (r)etrieve, (u)pdate, (d)elete, or e(x)it')
        user_command = input('Enter your selection here: ').strip().lower()
        print('---' * 50)
        active_session = True
        while active_session:
            if user_command in commands:
                if user_command == 'c' or user_command == 'create':
                    active_session = False
                    CRUD_REPL.create_contact(self)
                    self.main_menu()
                    pass
                elif user_command == 'l' or user_command == 'list':
                    active_session = False
                    CRUD_REPL.display_contact_names(self)
                    self.main_menu()
                    pass
                elif user_command == 'r' or user_command == 'retrieve':
                    active_session = False
                    try:
                        retrieve_name = input('Enter the name of the contact you would like to retrieve: ')
                        print(CRUD_REPL.retrieve_one_contact(self, retrieve_name))
                        active_session = False
                        self.main_menu()
                        pass
                    except KeyError:
                        print('That is not a valid entry, please enter a valid contact found within \'contacts.csv\'')
                        active_session = True
                elif user_command == 'u' or user_command == 'update':
                    active_session = False
                    try:
                        contact_name_input = input('Enter the name of the contact you would like to delete: ')
                        CRUD_REPL.update_contact(self, contact_name_input)
                        active_session = False
                        self.main_menu()
                    except KeyError:
                        print('That is not a valid entry, please enter a valid contact found within \'contacts.csv\'')
                        active_session = True
                elif user_command == 'd' or user_command == 'delete':
                    active_session = False
                    try:
                        del_name_input = input('Enter the name of the contact you would like to delete: ')
                        del_contact_info = self.contacts_dic[del_name_input]
                        CRUD_REPL.delete_contact(self, del_name_input)
                        active_session = False
                        self.main_menu()
                    except KeyError:
                        print('That is not a valid entry, please enter a valid contact within \'contacts.csv\'')
                        active_session = True
                elif user_command == 'x' or user_command.startswith('e'):
                    active_session = False
                    CRUD_REPL.update(self)
                    print('Thanks for using my program!')
                    break
            

if __name__ == "__main__":
    CRUD_REPL()