from data import DICTIONARY, LETTER_SCORES
import operator

def load_words():
    """Load dictionary into a list and return list"""
    wordlist = []
    with open(DICTIONARY) as file_obj:
        return [word.rstrip() for word in file_obj]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    word = word.rstrip()
    value = 0
    for letter in word:
        if letter.isalpha():
            value += LETTER_SCORES[letter.upper()]
    return value

def max_word_value(wordlist=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    wordscoredict = {}
    max_word_score = 0
    for word in wordlist:
        word = word.rstrip()
        wordscoredict[word] = calc_word_value(word)
        if calc_word_value(word) > max_word_score:
            max_word_score = calc_word_value(word)

    max_word_index = list(wordscoredict.values()).index(max_word_score)
    return list(wordscoredict.keys())[max_word_index]

if __name__ == "__main__":
    print(load_words())
 # run unittests to validate