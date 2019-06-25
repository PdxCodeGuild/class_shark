words = ['a', 'b', 'a', 'c', 'd']
stopwords = ['a', 'c']
for word in list(words):  # iterating on a copy since removing will mess things up
    if word in stopwords:
        words.remove(word)

print(words)