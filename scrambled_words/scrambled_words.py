#!/usr/bin/python3

'''
name: Joshua Rodriguez
email: ewized@gmail.com
problem: chapter 7 number 3 page 354
description: Scramble words from the paragraph and scramble it.
    - Handle punctuation.
'''

import random as rand

para = """\
We are a one of a kind server, as we do not use traditional method of playing.
We allow for all types of game styles. You are required to create an account
to join our network. The reason for this was to create features that no 
other server can provide, this is our game to website integration. We
reinvented the way you will play the game, as of this we use custom code that
differ from how you play on other servers. With this Each server that we run
is connected together, and you can connect to each server without 
reconnecting. We build our servers using high performance parts and custom
code to bring excellent experience to you.\
"""

# Function to shuffle the chars around
def shuffle(word):
    if len(word) <= 2:
        return word
    else:
        chars = list(word)
        rand.shuffle(chars)
        return list_to_string(chars)

# Function to scramble the word
def scramble(word):
    if len(word) < 3:
        return word

    first = word[:1]
    last = word[-1:]
    mid = word[1:-1]
    
    if last == "." or last == ",":
        last = word[-2:]
        mid = word[1:-2]

    return str(first) + str(shuffle(mid)) + str(last)

def list_to_string(lst) -> str:
    string = ""

    for char in lst:
        string += char

    return string;

# Grab this para and use a list to shuffle it
lst_para = para.strip().split()
shuffle_lst = []

for word in lst_para:
   shuffle_lst.append(scramble(word) + " ")

print(list_to_string(shuffle_lst))

