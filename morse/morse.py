#!/usr/bin/python3

'''
file: morse.py
name: Joshua Rodriguez
email: ewized@gmail.com
problem: number 21 page 432
description: Make a program that converts strings to morse code
    and convert morse code to strings. Create a dictionary to
    map the chars to the morse code equivalent.
'''


class Morse():
    morse_map = dict()
    word_map = dict()

    def __init__(self, input_file=open("morse.txt", "r")):

        for line in input_file:
            split = line.strip().split()
            self.morse_map[split[0]] = split[1]
            self.word_map[split[1]] = split[0]

    def to_morse(self, key):
        string = ""

        for code in key:
            if code == " ":
                string += " "
            else:
                string += self.morse_map[code.upper()] + " "

        return string

    def to_word(self, key):
        string = ""

        for code in key.split(" "):
            if code == "":
                string += " "
            else:
                string += self.word_map[code]

        return string


morse = Morse()

# print(morse.morse_map)
# print(morse.word_map)

print("1 - Convert to morse from word")
print("2 - Convert to word from morse")
result = int(input("> "))

if result == 1:
    word = input("Convert: ")
    print(morse.to_morse(word.strip()))
elif result == 2:
    print("Split code with space, use two spaces to create a space")
    word = input("Convert: ")
    print(morse.to_word(word.strip()).capitalize())
