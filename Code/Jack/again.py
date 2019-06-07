def again(question):
    choice = input(f'{question} y/n\n')
    if choice == 'n':
        return True
    elif choice == 'y':
        return False
    else:
        print('Incorrect input')
        return False
