#!/usr/bin/python3

'''
file: even_length.py
name: Joshua Rodriguez
email: ewized@gmail.com
problem: chapter 4 exercise 3 page 219
description: Given a var `S` containing a string of even length:
    a) Print out the first half
    b) Print out the last half
'''

S = "Year4000"

size = int(len(S))
half = int(size / 2)

print(S[:half])
print(S[half:size])

