from string import punctuation


def ari(i_char, i_words, i_sentences):
    return round(4.71*(i_char/i_words)+0.5*(i_words/i_sentences)-21.43)

def my_file(s_filename):

    d_char = {}
    d_words = {}
    i_sen = 0
    with open(s_filename, r) as f:
        content = f.read()
        content = content.strip()
        content = content.lower()
        # counts number of sentences by counting number of punc
        for i in range(len(content)):
            if content[i] in '.?!':
                i_sen += 1
        translator = str.maketrans('', '', punctuation)
        s = s.translate(translator)
        s = s.split()
