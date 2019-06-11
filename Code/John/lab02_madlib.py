# lab02_madlib.py
from random import choice
print("-" * 85)
print("\n" + "Welcome to my madlib!!! Please separate inputs with a space remember to have fun!")

madlib = True
while madlib:
    name = input("\n" + "Give me several personal names: ").lower().strip()
    pronoun = input("\n" + "Give me several 'relative' nouns e.g. brother/sister: ").lower().strip()
    verb = input("\n" + "And finally, give me some dangerous verbs: ").lower().strip()
    name = name.split()
    pronoun = pronoun.split()
    verb = verb.split()
    listen = True
    while listen:
        story = input("\n" + "Would you like to listen to your randomized story? (yes) or (no): ").lower().strip()
        while story not in ["yes", "no"]:
            print("Sorry that is not a valid response!" + "\n")
            story = input("\n" + "Would you like to listen to your story? (yes) or (no): ").lower().strip()
        if story == "yes":
            print("\n" + f"Hello, my name is {choice(name)} you killed my {choice(pronoun)} prepare to {choice(verb)}!")
        elif story == "no":
            listen = False
            another = input("\n" + "Would you like to create another story? (yes or (no): ").lower().strip()
            while another not in ["yes", "no"]:
                print("Sorry that is not a valid response!" + "\n")
                another = input("\n" + "Would you like to create another story? (yes or (no): ").lower().strip()
            if another == "yes":
                continue
            elif another == "no":
                madlib = False
                print("\n" + "Goodbye! I hope you had fun!!")
                print("-" * 85)
