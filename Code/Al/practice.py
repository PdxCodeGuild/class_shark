def cat_dog(word):
    cat_counter = 0
    dog_counter = 0
    for i in range(len(word)):
        if word[i:i+3] == 'cat':
            cat_counter += 1
        if word[i:i+3] =='dog':
            dog_counter += 1
    return cat_counter == dog_counter

def count_letter(letter, word):
    word_list = list(word)
    for let in word:
        if let != letter:
            while let in word_list:
                word_list.remove(let)
    return len(word_list)

def count_letter(letter, word):
    count = 0
    for i in word:
        if i == letter:
            count += 1
    return count

print(count_letter('a', 'abacadaef') + 1)
