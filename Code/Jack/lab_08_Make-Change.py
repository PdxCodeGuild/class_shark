class Change:
    """docstring for Change."""

    original_Amount = 0
    l_Coins = [('Quarters', 25),
               ('Dimes   ', 10),
               ('Nickels ', 5),
               ('Pennies ', 1)]
    l_Change = []


    def user_Def_Change(self):
        TF = True
        while TF:
            user_Coin_val = int(input('how many pennies is your new coin '
                                + 'worth? \n(e.g. 15 cents NOT .15)\n'))
            user_Coin_Name = input('What is the name of this coin?\n')
            while len(user_Coin_Name) < 8:
                user_Coin_Name += ' '
            user_Coin_Name = user_Coin_Name.title()
            self.l_Coins.append((user_Coin_Name,user_Coin_val))
            choice = input('Would you like to add another new coin? y/n \n')
            if choice == 'y':
                TF = True
            elif choice == 'n':
                TF = False
            else:
                print('Invalid Input')
        self.l_Coins = sorted(self.l_Coins,
                              key = self.get_index_two,
                              reverse = True)


    def get_index_two(self, in_List):
        return in_List[1]


    def change_Pennies(self):
        num_Of_Pennies = int(input('How many pennies do you have? '))
        self.original_Amount = num_Of_Pennies
        self.l_Change = self.make_Change(num_Of_Pennies)
        self.show_Change()
        self.do_More_Choice()


    def change_Dollars(self):
        amount = float(input('Please enter how much money you\n '
                            + 'want me to make change for: '
                            + '(e.g. $1.25)\n$'))
        amount = int(round((amount*100), 0))
        self.original_Amount = amount
        self.l_Change = self.make_Change(amount)
        self.show_Change()
        self.do_More_Choice()


    def do_More_Choice(self):
        TF = True
        while TF:
            choice = input('Would you like to do more to your '
                                + 'current amount? y/n\n')
            if choice == 'y':
                self.do_More_Menu()
            elif choice == 'n':
                TF = False
            else:
                print('\ninvalid input\n')


    def do_More_Menu(self):
        menu_Choice = int(input('Please make a selection '
                        + 'from the following:\n'
                        + 'Add:         1\n'
                        + 'Subtract:    2\n'))
        if menu_Choice == 1:
            self.add_More()
        elif menu_Choice == 2:
            self.subtract_More()
        else:
            print('incorrect input')


    def add_More(self):
        t_add = float(input('How much would you like to add? '
                            + '(e.g. 1.26)\n'))
        t_add = int(round((t_add*100), 0))
        t_add += self.original_Amount
        self.original_Amount = t_add
        self.l_Change = self.make_Change(t_add)
        self.show_Change()


    def subtract_More(self):
        t_subtract = float(input('How much would you like to subtract? '
                            + '(e.g. 1.26)\n'))
        t_subtract = int(round((t_subtract*100), 0))
        t_subtract = self.original_Amount - t_subtract
        self.original_Amount = t_subtract
        self.l_Change = self.make_Change(t_subtract)
        self.show_Change()


    def make_Change(self, amount):
        num_Of_Pennies = amount
        rem = []
        i = 0
        t_List = []

        rem.append(num_Of_Pennies % self.l_Coins[i][1])
        t_List.append(num_Of_Pennies // self.l_Coins[i][1])
        i += 1

        while i < len(self.l_Coins):
            k = i - 1
            rem.append(rem[k] % self.l_Coins[i][1])
            t_List.append(rem[k] // self.l_Coins[i][1])
            i += 1
        return t_List


    def show_Change(self):
        i = 0
        while i < len(self.l_Coins):
            print(f'{self.l_Coins[i][0]}\t{self.l_Change[i]}')
            i += 1
        print('')


def menu_One():
    menu_Choice = int(input('Welcome to \'Make Change\'!\n'
                    + 'Please make a selection from the following:\n'
                    + 'I make change from your pennies:     1\n'
                    + 'I make change from your dollars:     2\n'
                    + 'You enter in some new types of\n'
                    + 'coins and THEN I make change!        3\n'))
    return menu_Choice


def again():
    choice = input('would you like to make change? y/n\n')
    if choice == 'y':
        return True
    elif choice == 'n':
        print('\nGoodBye!\n')
        return False
    else:
        print('\nincorrect input:\n')
        return True


TF = True
ch = Change()
while TF:
    choice = menu_One()
    if choice == 1:
        ch.change_Pennies()
    elif choice == 2:
        ch.change_Dollars()
    elif choice == 3:
        ch.user_Def_Change()
    else:
        print('\ninvalid input\n')
    TF = again()
