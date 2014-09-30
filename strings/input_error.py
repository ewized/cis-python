#!/usr/bin/python3

'''
file: input_error.py
name: Joshua Rodriguez
email: ewized@gmail.com
problem: chapter 4 exercise 12 page 220
description: Why is it generating the error:
    "ValueError: too many values to unpack."

    first, second = input("two spaced-separated numbers: ")
'''

# The reason is the space counts as an input
first, space, second = input("two spaced-separated numbers: ")

print(first, " ", second)

