#!/usr/bin/python3

'''
file: monty_python.py
name: Joshua Rodriguez
email: ewized@gmail.com
problem: chapter 4 execise 1 page 219
description: Given the string 'Monty Python':
    a) Print the first char
    b) Print the last char
    c) Using the function len() print the list char
    d) Print 'Monty'
'''

monty = "Monty Python"

print(monty[:1])
print(monty[-1:])
print(monty[len(monty) - 1:])
print(monty[0:5])
