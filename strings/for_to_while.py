#!/usr/bin/python3

'''
file: for_to_while.py
name: Joshua Rodriguez
email: ewized@gmail.com
problem: chapter 4 exercise 10 page 220
description: In the following program, replace the `for` with
    `while` loop.

    S="I had a cat named amanda when I was little"
    count = 0
    for i in S:
        if i == 'a':
            count += 1

    print(count)
'''

S="I had a cat named amanda when I was little"
count = 0
iterable = 0

while iterable < len(S):
    
    if S[iterable] == 'a':
        count += 1

    iterable += 1

print(str(count))

