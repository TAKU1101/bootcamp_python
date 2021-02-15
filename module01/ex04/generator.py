from random import randint
from collections import Counter


def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    if not isinstance(text, str):
        yield "ERROR"
        return
    word_list = text.split(sep)
    if option == "shuffle":
        shuffle_list = []
        size = len(word_list)
        for i in range(size):
            shuffle_list.append(word_list.pop(randint(0, len(word_list) - 1)))
        word_list = shuffle_list
    elif option == "ordered":
        word_list.reverse()
    elif option == "unique":
        countDir = Counter(word_list)
        word_list = countDir.keys()
    for word in word_list:
        yield word
