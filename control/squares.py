'''
name: Joshua Rodriguez
email: ewized@gmail.com
file: squares.py
problem: chapter 2 number 22 page 149
description: Create a program that prompts for a positive number greater than 2 
    (check if the input is greater than 2) and then keeps taking the square root of that
    number until the square root is less than 2, print the value of the square root each time
'''
import math

number = input("Enter a number greater than 2: ")

# Check the number
while int(number) <= 2:
    number = input("ENTER A NUMBER GREATER THAN 2: ")

# Print the squares
while not int(number) < 2:
    number = math.sqrt(int(number))
    print(str(number))
