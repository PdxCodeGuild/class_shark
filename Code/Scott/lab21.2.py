"""
Name:           Scott Tran
Date            6/24/2019
Assignment:     Write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.

"""
from pprint import pprint
from string import punctuation
from collections import Counter

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def listmaker():
    
    with open('dracula.txt', 'r') as my_book:
        all_words = []
        lines = my_book.readlines()[0:1000]# in testing you can use '[0:10]' after 'readlines()'  for the first 10 lines
        
        for i in range(len(lines)):
            all_words.extend(lines[i].lower().split())
        return all_words
        
 
def no_punct(x):
    for s in list(x):
        translator = str.maketrans('', '', punctuation)
        string_without_punct = s.translate(translator) # I am a string with punctuation
    return x


def remove_list(x):
    for i in list(x):
        if i in stopwords:
            x.remove(i)
    return x       

y = remove_list(no_punct(listmaker()))

pairs = list(zip(y, y[1:]))

x = Counter(pairs)
pprint(x.most_common(10))