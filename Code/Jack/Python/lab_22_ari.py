from string import punctuation, ascii_letters as AL


def ari(i_char, i_words, i_sentences):
    return round(4.71*(i_char/i_words)+0.5*(i_words/i_sentences)-21.43)


def my_file(s_filename):

    d_char = {}
    d_words = {}
    i_sen = 0
    char_count = 0
    word_count = 0
    with open(s_filename, r) as f:
        content = f.read()
        content = content.strip().lower()
        # counts number of sentences by counting number of punc
        for i in range(len(content)):
            if content[i] in '.?!':
                i_sen += 1
        translator = str.maketrans('', '', punctuation)
        content = content.translate(translator)
        tl_words = content.split()
        for word in tl_words:
            d_words[word] = d_words.get(word, 0) + 1
            word_count += 1
        ts_char = content.replace(' ','')
        for i in range(len(ts_char)):
            if ts_char[i] in AL:
                d_char[ts_char[i]] = d_char.get(ts_char, 0) + 1
                char_count += 1
        ari_val = ari(char_count, word_count, i_sen)
