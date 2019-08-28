#LAB 21 COUNT WORDS
#1 open file
#2 make everything lowercase
    #2b strip punctuation
    #2c split into list of words

#3 dictionary will have words as keys and counts as values. if word isnt in dictionary than add it
#4 print the most frequent top 10 out of their counts

import string
import collections

STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

with open('meditations.txt','r') as f:
    m = f.read()
    m = m.lower()
    translator = str.maketrans('', '', string.punctuation)
    m = m.translate(translator)
    m = m.split()

def wordcount(words):
    wordcount = collections.Counter(m)
    print (wordcount)
    top_ten = wordcount.most_common(10)
    print(top_ten)
    #this counts ALL words (including the stopwords)
    #this will also print out the top 10 words including stopwords

def wordlist(m):
    word_dict = {}

    for word in m:
        if word not in STOPWORDS:
            word_dict[word] = word_dict.get(word,0) + 1  
    return word_dict

    #whether the words in the file m (meditations) has any of the words in STOP WORDS'''

def topten():
    wordcount = {}
    for word in m:
        if word not in STOPWORDS:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word]+= 1
    n_print = int(input("How many most commons words to print:  "))
    print("\nOK. The {} most common words are as follows\n".format(n_print))
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(n_print):
        print(word, ": ", count)