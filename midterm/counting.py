'''
name: Joshua Rodriguez
email: ewized@gmail.com
file: counting.py
problem: Midterm #1
description: Write a program that will take a string as input
    and will perform the following functions.
    - Print the number of spaces in the string
    - Print the number of lowercase letters
    - Print the number of punctuation marks
'''
string = "This is a string of chars... It also has other things in it."

def number(haystack):
    # spaces | lower | punctuation
    count = [0, 0, 0]

    for char in haystack:
        if char.islower():
            count[1] += 1

        if char == " ":
            count[0] += 1

        if not (char.isalpha() and char.isdigit()):
            count[2] += 1

    # Lets print them out
    print("Number of spaces:", count[0])
    print("Number of lower chars", count[1])
    print("Number of punctuation", count[2])

number(string)

