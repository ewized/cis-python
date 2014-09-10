'''
name: Joshua Rodriguez
email: ewized@gmail.com
problem: chapter 2 number 1 page 144
description: How many three-digit numbers are divisible by 7? Write a program to print it out
'''
count = 0

for i in range(100, 999):
    if i % 17 == 0:
        count += 1
        print(str(i), end=", ")

print("their were " + str(count) + " numbers divisible by 17.")
