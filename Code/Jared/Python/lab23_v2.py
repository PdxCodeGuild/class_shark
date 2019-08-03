'''
lab23
convert lines in file into a dictionary
'''

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)


csv = [] # creating our list of lists

keys = lines[0]
keys = keys.split(',')

for i in range(1, len(lines)): ### iterates through list starting from index 1

    row = lines[i]
    row = row.split(',')

    row = dict(zip(keys, row)) # creates dictionary
    csv.append(row)

contacts = []
name = input('Enter your name: ')
contacts.append(name)
phone = input('Enter your phone number: ')
contacts.append(phone)
age = input('Enter your age: ')
contacts.append(age)
occupation = input('Enter your occupation: ')
contacts.append(occupation)

csv[contacts['name']] = contacts[i]

csv.append(contacts)
# csv.append(row)

print(csv)
with open('contacts2.csv', 'w') as file:
    lines = file.write(str(csv))
#
#
#
csv_to_dict = {}
file_name = 'contacts2.csv'
csv_to_dict[file_name] = csv

for filename, csv in csv_to_dict.items():
    print(filename)
    for row in csv:
        print(row)

# print(keys)
# print(lines)
# print(csv)
# contacts = ''
#

#
#
#
# name = input('Enter your name: ')
# # name.append(contacts)
# phone = input('Enter your phone number: ')
# # phone.append(contacts)
# age = input('Enter your age: ')
# # age.append(contacts)
# occupation = input('Enter your occupation: ')
# # occupation.append(contacts)
#
# contacts = name + phone + age + occupation
# contacts.split(',')
