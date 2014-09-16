"""
Name: Joshua Rodriguez
File: math.py
Email: ewized@gmail.com
Description: Take the number, add 2, multiply by 3 subtract 6 and divide by 3.
     You should get the number you started with.
"""

answer = input("Enter a number: ")

print("You started with: " + answer)

answer = (((int(answer) + 2) * 3) - 6) / 3

print("You ended with: " + str(int(answer)))
