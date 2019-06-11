# practice_strings_p1&2.py

def double_letters(text):
    #doubled = []
    #for letter in text:
    #    doubled.append(letter + letter)
    #return "".join(doubled)
    return "".join([letter + letter for letter in text])


def missing_char(text):
    missing = []
    for i in range(len(text)):
        #text = text.replace(text[i], "")
        left = text[0:i] #can leave out 0 here :i
        right = text[i+1:]
        print(i, "left", left, "right", right)
        missing.append(left + right)
    return missing

print(double_letters("hello"))

print(missing_char("kitten"))
