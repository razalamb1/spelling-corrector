# Python Spelling Corrector
import numpy as np
import re
import time


def make_dictionary(dictionary_file):
    with open("english.txt") as f:
        english = []
        for line in f:
            line = line[:-1]
            english.append(line)
            pass
        pass
    return english


def tokenization(text_string):
    word_list = re.split("(\W+)", text_string)
    return word_list


def detokenization(word_list):
    doc = ""
    doc = doc.join(word_list)
    return doc


def calc_distance(word, word2):
    rows = len(word) + 1
    columns = len(word2) + 1
    lev = np.zeros((rows, columns)).astype(int)
    for i in range(rows):
        lev[i, 0] = i
        pass
    for i in range(columns):
        lev[0, i] = i
        pass
    for i in range(1, rows):
        for j in range(1, columns):
            if word[i - 1] == word2[j - 1]:
                lev[i, j] = min(lev[i - 1, j] + 1, lev[i, j - 1] + 1, lev[i - 1, j - 1])
                pass
            else:
                lev[i, j] = min(
                    lev[i - 1, j] + 1, lev[i, j - 1] + 1, lev[i - 1, j - 1] + 1
                )
                pass
            pass
        pass
    return lev[rows - 1, columns - 1]


def check_word(index, list, english):
    if len(list[index]) == 0:
        return False
    elif (
        not re.fullmatch("(\W+)", list[index])
        and list[index] not in english
        and not list[index][0].isupper()
        and not list[index][0].isnumeric()
    ):
        return True
    else:
        return False


def spelling_corrector(text_string, dictionary_file):
    english = make_dictionary(dictionary_file)
    word_list = tokenization(text_string)
    for i in range(len(word_list)):
        if check_word(i, word_list, english):
            distlist = []
            for j in english:
                distlist.append(calc_distance(word_list[i], j))
                pass
            replace = english[distlist.index(min(distlist))]
            word_list[i] = replace
            pass
        pass
    doc = detokenization(word_list)
    return doc
    pass
