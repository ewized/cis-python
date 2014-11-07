'''
name: Joshua Rodriguez
email: ewized@gmail.com
file: standard_deviation.py
problem: Midterm #3
description: Standard deviation create a program to do that.
'''
import math

lst = [1, 3, 4, 6, 9, 19]

for i in range(0, len(lst)):
    print(i, "")

def get_average(lst):
    avg = 0

    for i in range(0, len(lst)):
        avg += lst[i];

    return avg / len(lst)

def get_summation(lst):
    avg = get_average(lst)
    summation = 0

    for i in range(0, len(lst)):
        summation += (lst[i] - avg)**2

    return summation

def get_devation(lst):
    summation = get_summation(lst)
    return math.sqrt(summation / (len(lst) - 1))


print("The deviation of", str(lst), "is", get_devation(lst))
