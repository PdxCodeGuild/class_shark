"""
Name:           Scott Tran
Date            6/24/2019
Assignment:     Compute the ARI for a given body of text loaded in from a file. The automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. The general formula to compute the Automated Readability Index (ARI).

"""
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

def listmaker():
    
    with open('dracula.txt', 'r') as my_book:
        sentences = 0
        lines=0
        words=0
        characters=0
        for line in my_book:
            wordslist=line.split()
            lines=lines+1
            words=words+len(wordslist)
            characters += sum(len(word) for word in wordslist)
            sentences += line.count('.') + line.count('!') + line.count('?')
    ari = round((4.71*(characters/words))+ (0.5*(words/sentences))- 21.43,0)
    print(f"There are {sentences} sentences, {words} words, and {characters} characters in this text with an ARI score of {round(ari,0)}.  This corresponds to a {ari_scale[ari]['ages']} age and {ari_scale[ari]['grade_level']} reading level. ")




listmaker()