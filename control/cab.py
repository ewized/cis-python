'''
name: Joshua Rodriguez
email: ewized@gmail.com
file: cab.py
problem: chapter 2 number 25 page 149
description: Find the two-digit number such that when you square it, the
    resulting three-digit number has its rightmost two digits the same as
    the original two-digit number. That is for a number AB, AB * AB = CAB
    for some C.
'''
import math

should_loop = True
number = 9
found = 0

while should_loop and number < 99:
    number += 1

    square = int(number) ** 2
    #print(str(number) + " | " + str(square)[-2] + str(square)[-1])

    if str(number) == str(square)[-2] + str(square)[-1]:
        found += 1
        print(str(number) + " = " + str(square))
else:
    if found == 0:
        print("Their are no numbers possible in the form AB * AB = CAB")
