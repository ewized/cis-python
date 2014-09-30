#!/usr/bin/python3

'''
file: fun_with_splicing.py
name: Joshua Rodriguez
email: ewized@gmail.com
problem: chapter 4 exercise 29 page 222
description: Given the string `abcdefghij`, write a one line
    of code that will print

    a) 'jihgfedcba'
    b) 'adgj'
    c) 'igeca'
'''

string = "abcdefghij"

print(string[::-1], string[::3], string[-2::-2])

