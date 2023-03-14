#!/usr/bin/env python3

def return_evens(num_list):
    evens_list = [n for n in num_list if n % 2 == 0]
    return evens_list
def make_exclamation(sentence_list):
    new_sentences = [n + "!" for n in sentence_list]
    return new_sentences

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))