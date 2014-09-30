#!/usr/bin/python3

'''
file: string_operators.py
name: Joshua Rodriguez
email: ewized@gmail.com
problem: chapter 4 exercise 23 page 222
description: Operators for strings!
    a) You want a full line of `#` that is 80 char's
        using the `+` operator.
    b) You want a column full of `#` of 30 lines
        using the `\n` and `*`
'''

line = "#"
for i in range(1, 80):
    line += "#"

print(str(line))
# Debug test the length of the string
# print(len(line)

print("#\n" * 30)

