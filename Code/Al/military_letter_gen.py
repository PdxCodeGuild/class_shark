# filename: "military_letter_gen.py"
letter_dict = {'a': 'alpha', 'b': 'bravo', 'c': 'charlie'}
user_input = input('Type some letters: ')
out_string = ''
for letter in user_input:
    out_string += letter_dict[letter] + ' '
print(out_string)
