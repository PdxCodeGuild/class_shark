# iphone_counter.py
with open('how_many_iphones.csv') as f: # briefly open the file
    iphone_info = f.read() # get it as a string

iphone_info = iphone_info.split('\n') # make a list, split on newline
iphone_info.pop(-1) # remove the empty string at the end

iphone_list = []
for row in iphone_info:
    # make a list of lists, each inner list has two strings
    iphone_list.append(row.replace(' ', '').split(','))

list_of_dictionaries = []
key_row = iphone_list[0] # the first list is [key1, key2]
for value_row in iphone_list[1:]: # each following list is [value1, value2]
    # make a bunch of dictionaries with the same keys and different values
    list_of_dictionaries.append({key_row[0]: value_row[0], key_row[1]: value_row[1]})
print(list_of_dictionaries) # this data is easier to analyze
