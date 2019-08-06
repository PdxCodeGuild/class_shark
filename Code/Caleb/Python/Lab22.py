# Lab 22: Compute Automated Readability Index
# Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows:

# ARI Formula
# The score is computed by multiplying the number of characters divided by the number of words by 4.17, adding the number of words divided by the number of sentences multiplied by 0.5, and subtracting 21.43. If the result is a decimal, always round up. Scores greater than 14 should be presented as having the same age and grade level as scores of 14.

# Scores correspond to the following ages and grad levels:
#     Score  Ages     Grade Level
#      1       5-6    Kindergarten
#      2       6-7    First Grade
#      3       7-8    Second Grade
#      4       8-9    Third Grade
#      5      9-10    Fourth Grade
#      6     10-11    Fifth Grade
#      7     11-12    Sixth Grade
#      8     12-13    Seventh Grade
#      9     13-14    Eighth Grade
#     10     14-15    Ninth Grade
#     11     15-16    Tenth Grade
#     12     16-17    Eleventh grade
#     13     17-18    Twelfth grade
#     14     18-22    College
# Once you’ve computed the ARI score, you can use the following dictionary to look up the age range and grade level.
# ari_scale = {
#      1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
#      2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
#      3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
#      4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
#      5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
#      6: {'ages': '10-11', 'grade_level':    '5th Grade'},
#      7: {'ages': '11-12', 'grade_level':    '6th Grade'},
#      8: {'ages': '12-13', 'grade_level':    '7th Grade'},
#      9: {'ages': '13-14', 'grade_level':    '8th Grade'},
#     10: {'ages': '14-15', 'grade_level':    '9th Grade'},
#     11: {'ages': '15-16', 'grade_level':   '10th Grade'},
#     12: {'ages': '16-17', 'grade_level':   '11th Grade'},
#     13: {'ages': '17-18', 'grade_level':   '12th Grade'},
#     14: {'ages': '18-22', 'grade_level':      'College'}
# }
# The output should look something like the following:
# --------------------------------------------------------
# The ARI for gettysburg-address.txt is 12
# This corresponds to a 11th Grade level of difficulty
# that is suitable for an average person 16-17 years old.
# --------------------------------------------------------
from string import punctuation
from string import ascii_letters

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

print('Welcome to Lab 22 - Compute Automated Readability Index. A program written in python by Caleb Mealey')
print('This program will compute the ARI of a given text file. The ARI (automated readability index) is a formula for computing the U.S. grade level for a given block of text.')

def ARI(characters, words, sentences):
'''
The equation to plug in our values for the characters, words, sentences, and output the calculated Automated Readability Index.
'''
    return round(4.71*(characters/words)+0.5*(words/sentences)-21.43)

def openfile(file_location):
    with open(f'{file_location}', 'r', encoding="utf8") as b:
        book_text = b.read()
        book_text = book_text.strip().lower()
        # Initialize the counting variables
        char_count = 0
        words_count = 0
        sentences_count = 0
        # Count the number of sentences by the various punctuation which ends a sentence ".?!"
        for i in range(len(book_text)):
            if book_text[i] in ['.','?','!']:
                sentences_count += 1
        translator = str.maketrans('', '', punctuation)
        book_text_no_punc = book_text.translate(translator)
        book_text_no_punc_ls = book_text_no_punc.split()
        # After stripping the text of punctuation, and separating it into a list, we can now loop through and count the total amount of words
        for words in book_text_no_punc_ls: 
            words_count += 1
        char_string = book_text_no_punc.replace(' ', '')
        # After replacing all spaces with no spaces, we can now loop through and count all of the ASCII characters.
        for x in range(len(char_string)):
            if char_string[x] in ascii_letters:
                char_count += 1
        ARI_val = ARI(char_count,words_count, sentences_count)
        print('---' * 50)
        print(f'The ARI for the following text, {file_location}, is: {ARI_val}')
        print(f'This corresponds to a {ari_scale[ARI_val]["grade_level"]} grade level of difficulty')
        print(f'That is suitable for an average person {ari_scale[ARI_val]["ages"]} years old.')
        print('---'* 50)

if __name__ == "__main__":
    openfile('./assets/AdventuresofHuckleberryFinn.txt')
    openfile('./assets/TheKingJamesBible.txt')
    openfile('./assets/MobyDick.txt')
    openfile('./assets/TheAdventuresofSherlockHolmes.txt')