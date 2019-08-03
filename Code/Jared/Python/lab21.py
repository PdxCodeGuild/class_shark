from string import punctuation
stopwords = ['thine', 'mine', 'may', 'art', 'yet', 'shall', 'thy', 'thou', 'thee', 'doth', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


"""
Version 1
Count words and return in dictionary; print top 10

"""

def dict_1(words):
    d = {}
    for word in words:
        if word not in stopwords:
            d[word] = d.get(word, 0) + 1
    return d


with open('sonnets.txt', 'r') as f:
    contents = f.read()
    contents = contents.lower()
    translator = str.maketrans('', '', punctuation)
    contents = contents.translate(translator)
    contents = contents.split()

    word_dict = dict_1(contents)

# word_dict is a dictionary where the key is the word and the value is the count
    words = list(word_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])



"""
Version 2
Count how often unique pair of words is used, print top 10
"""
def dict_2(words):
    pairs = ''
    d = {}
    for i in range(len(words)-1):
        if i not in stopwords: # doesn't work because it looks at index and not values?
            pairs = words[i] + " " + words[i + 1]
            d[pairs] = d.get(pairs, 0) + 1

    return d

with open('sonnets.txt', 'r') as f:
    contents = f.read()
    contents = contents.lower()
    translator = str.maketrans('', '', punctuation)
    contents = contents.translate(translator)
    contents = contents.split()

    pair_dict = dict_2(contents)

# word_dict is a dictionary where the key is the word and the value is the count
    words = list(pair_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])
