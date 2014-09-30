#!/usr/bin/python3

'''
file: five_strings.py
name: Joshua Rodriguez
email: ewized@gmail.com
problem: chapter 4 exercise 14 page 221
description: Five strings methods manipulate case:
    a) Describe what `capitalize` does.
    b) Describe what `title` does.
    c) Describe what `swapcase` does.
    d) Describe what `upper` does.
    e) Describe what `lower` does.
'''

s1, s2, s3, s4 = "concord", "souix city", "HONOLULU", "TopHat"

# a, will make the first char uppercase
print("Capitalize:", s1.capitalize())

# b, will make the first char of each word uppercase
print("Title:", s2.title())

# c, will switch each lowercase char to uppercase and visa versa
print("Swapcase:", s4.swapcase())

# d, will make the letters uppercase
print("Upper:", s1.upper())

# e, will make the letters lowercase
print("Lower:", s3.lower())

