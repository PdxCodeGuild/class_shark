def again(question):
    TF = True
    while TF:
        choice = input(f'{question} y/n\n')
        if choice == 'n':
            TF = False
            return True
        elif choice == 'y':
            TF = False
            return False
        else:
            print('Incorrect input')
