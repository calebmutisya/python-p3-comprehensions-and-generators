#!/usr/bin/env python3

def return_evens(num_list):
    evens=[num for num in num_list if num%2 ==0]
    return evens



def make_exclamation(sentence_list):
    exclaimed=[word + "!" for word in sentence_list]
    return exclaimed

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
