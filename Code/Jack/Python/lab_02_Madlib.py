import random


# noun = 2
# person = 2
# verb = 5
# holiday = 1
# color = 3
# adjective = 2
# vegetable = 1

while True:
    nouns = input("Please give me two nouns: ").split()
    person = input("Please give me to names: ").split()
    verb = input("Please enter five verbs: ").split()
    holiday = input("please enter a holiday: ")
    color = input('Please enter three colors: ').split()
    adjective = input('Please enter two adjectives: ').split()
    vegetable = input('Please enter a vegetable: ')


    print(f'Did you ever have one of those {random.choice(nouns)}s? Well today {random.choice(person)} did! Mom wanted to {random.choice(verb)} {random.choice(nouns)} for {holiday}. Not just any lights, {random.choice(color)} lights. {random.choice(adjective)} {random.choice(color)} lights! {random.choice(adjective)} bright red lights. The only problem, they are a {random.choice(verb)}ed mess! Not to mention that there are some {vegetable}, yellow and green lights {random.choice(verb)}ed in."{random.choice(person)}!" I yell! "This can\'t be done! She could {random.choice(verb)}!" I was right and went out and {random.choice(verb)}ed some new shiny {random.choice(color)} lights!')
    choice = input('Would you like to go again? yes/no: ')
    if choice == 'no':
        break
