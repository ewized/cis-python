#!/usr/bin/python3

'''
file: scrambled.py
name: Joshua Rodriguez
email: ewized@gmail.com
problem: chapter 5 project 1 page 252 and 253
description: Take in a file that contains a paragraph, scramble
    the internal words of each word and then write the result to
    a new file.

    You need to handle punctuation. You have 3 ways of solving the
    problem.

    a) Easiest: Rotate the letters by 13 (know as ROT13)
    d) Harder: For each letter choose a random number and rotate
        change the position by a random amount.
    c) Hardest: Improve on a and b by a method of your choice
'''

import random as rand

# Open the file is input is not there create one
try:
    in_text = open("in.txt", "r")
    out_text = open("out.txt", "w")
except IOError:
    print("File in.txt does not exist creating default one.")
    in_file = open("in.txt", "w")

    string = """\
We are a one of a kind server, as we do not use traditional method of playing.
We allow for all types of game styles. You are required to create an account
to join our network. The reason for this was to create features that no 
other server can provide, this is our game to website integration. We
reinvented the way you will play the game, as of this we use custom code that
differ from how you play on other servers. With this Each server that we run
is connected together, and you can connect to each server without 
reconnecting. We build our servers using high performance parts and custom
code to bring excellent experience to you.\
""".strip()

    print(string, file = in_file)
    in_file.close()
    in_text = open("in.txt", "r")
    out_text = open("out.txt", "w")

# Function to shuffle the chars around
def shuffle(word):
    if len(word) == 1:
        return word
    else:
        half = int(len(word) / 2)
        # First half in reverse
        first = word[:half][::-1]
        # Last half in reverse
        last = word[half:len(word)][::-1]

        # First + Last in reverse
        return str(first+last)[::-1]

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

# Read the input and write the scrambled words to the output
for line in in_text:
    line = line.strip()
    new_line = ""

    for word in line.split(" "):
        new_line += scramble(word) + " "

    print(new_line, file = out_text)

# Close open files
in_text.close()
out_text.close()
