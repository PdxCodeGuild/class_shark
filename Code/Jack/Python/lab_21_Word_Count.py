from string import punctuation


STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


def ver_one(s):
    d_word = {}
    for word in s:
        if word not in STOPWORDS:
            d_word[word] = d_word.get(word, 0) + 1

    return d_word


def ver_two(s):
    words = ''
    d_word = {}
    for i in range(len(s)-1):
        words = s[i] + ' ' + s[i+1]
        d_word[words] = d_word.get(words, 0) + 1

    return d_word


def ver_three(s, key_word):
    td_d = {}
    for i in range(len(s)-1):
        if s[i] == key_word:
            td_d[s[i+1]] = td_d.get(s[i+1], 0) + 1

    return td_d



def not_in_SW(s):
    return [word for word in s if word not in STOPWORDS]


def main():
    with open('./Images/A Princess of Mars.txt', 'r') as f:
        s = f.read()
        s = s.lower()
        translator = str.maketrans('', '', punctuation)
        s = s.translate(translator)
        s = s.split()
        # tl_s = not_in_SW(s)
        # word_dict = ver_one(tl_s)
        # word_dict = ver_two(tl_s)
        key_word = input('Please enter word: ')
        key_word = key_word.translate(translator)
        word_dict = ver_three(s, key_word)

    # word_dict is a dictionary where the key is the word and the value is the count
        words = list(word_dict.items())  # .items() returns a list of tuples
        words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
        for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
            print(words[i])


main()
