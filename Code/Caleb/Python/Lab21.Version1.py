'''
Lab 21: Count Words
Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg. Download it as a UTF-8 text file.

Open the file.
Make everything lowercase, strip punctuation, split into a list of words.
To strip punctuation:

from string import punctuation
s = 'I $am a !string with punc&^%*tuation!'
translator = str.maketrans('', '', punctuation)
string_without_punct = s.translate(translator) # I am a string with punctuation
Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
Print the most frequent top 10 out with their counts. You can do that with the code below.
# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
You'll find that the most common words aren't particularly interesting (lots of 'I's, 'the', 'and', 'he', 'she', and 'but's). To get more relevant words, remove stop words from your text.

'''
from string import punctuation
STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

print('Welcome to Version 1 of Lab 21 - Count Words. A program written in python by Caleb Mealey')

def openfile(file_location):
    print(f'The 10 most reoccuring words found in {file_location} outside of the standard common words listed in the "stop words" list are:')
    with open(f'{file_location}', 'r', encoding="utf8") as b:
        book_text = b.read()
        book_text = book_text.lower()
        translator = str.maketrans('', '', punctuation)
        book_text_no_punc = book_text.translate(translator)
        book_text_no_punc_ls = book_text_no_punc.split()
        word_dict = {}
        for word in book_text_no_punc_ls:
            if word not in STOPWORDS:
                word_dict[word] = word_dict.get(word,0) + 1

        words = list(word_dict.items()) # .items() returns a list of tuples
        words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
        for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
            print(words[i])
    print("---"*50)


if __name__ == "__main__":
    openfile('./assets/AdventuresofHuckleberryFinn.txt')
    openfile('./assets/TheKingJamesBible.txt')
    openfile('./assets/MobyDick.txt')
    openfile('./assets/TheAdventuresofSherlockHolmes.txt')