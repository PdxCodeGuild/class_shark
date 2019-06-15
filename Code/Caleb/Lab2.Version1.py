## Lab 2: Mad Libs

## Write a simple program that prompts the user for several ## inputs then
## prints a [Mad Lib](https://en.wikipedia.org/wiki/Mad_Libs) as the result.


location = str(input("Enter a location, preferably a real place: "))
famous_person = str(input("Enter the name of somebody famous: "))
adjective = str(input("Enter a adjective: "))
sound = str(input("Enter a sound: "))
animal_a = str(input("Enter an animal: "))
animal_b = str(input("Enter an animal you don't enjoy eating, different from the one you just entered: "))
animal_c = str(input("Enter an animal who's eating style most resembles your own: "))
verb_1 = str(input("Enter a verb: "))
type_of_person = str(input("Enter a type of person (please refrain from any deratory language): "))
noun = str(input("Enter a noun: "))
verb_2 = str(input("Enter another verb, different from your first: "))
store = str(input("Enter the name of a store: "))
race_of_people = str(input("Enter the race of a group of people, please no racist or derogatory langauge: "))

Alright_or_Terrible = int(input("Enter 1 if you're feeling alright: "))
if Alright_or_Terrible == 1:
	Alright_or_Terrible = "alright"
else:
	Alright_or_Terrible = "terrible"

famous_woman = str(input("Enter a famous woman: "))
verb_3 = str(input("Enter a verb: "))
group_of_people = str(input("Enter a group of people: "))
ed_verb = str(input("Enter a verb ending in 'ed': "))
accomplishment = str(input("Enter a significant accomplishment: "))
plural_noun = str(input("Enter a plural noun: "))
unsuccessful_athlete = str(input("Enter your least favorite athlete: "))
place = str(input("Enter your favorite place: "))
game = str(input("Enter your least favorite game: "))
setting = str(input("Enter a the name of a peaceful setting: "))

Story = 'Just waking up in the ' + location + ', gotta thank ' + famous_person + '. I don\'t know, but today seems kinda ' + adjective + '. No ' + sound + ' from the ' + animal_a + ', no smog, and momma cooked a breakfast with no ' + animal_b + '. I got my grub on, but I didn\'t ' + animal_c + ' out. Finally got a call from a girl I want to ' + verb_1 + '. Hoooked it up for later as I hit the door, thinking, \"Will I live to see another ' + type_of_person + '? I gotta go\" \'cause I got me a ' + noun + ', and if I hit the switch I can make the ass ' + verb_2 + '. Had to stop at a ' + store + '; looking in the mirror, not a ' + race_of_people + ' in sight and everything is ' + Alright_or_Terrible + '. I got a beep from ' + famous_woman + ' and she can ' + verb_3 + ' all night. Calling up the ' + group_of_people + ' and I\'m asking y\'all, \"Which\"' + place + ' are y\'all playing ' + game + '? Get me on the court ' + setting + ' and I\'m trouble. Last week, ' + ed_verb + ' around and got a ' + accomplishment + '. Freaking ' + plural_noun  + ' every way like ' + unsuccessful_athlete + '. I can\'t believe today was a ' + adjective + ' day.'

Interest_in_story = input("Enter y if you would like to hear your story: ")

print(Story)
