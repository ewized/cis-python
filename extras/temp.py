"""
name: Joshua Rodriguez
email: ewized@gmail.com
description: Write a program that will prompt a user to enter 
        a temperature as an integer. Your program will print 
        "it is hot" is the temperature is over 100, "it is cold"
        if the temperature is under 60, and "it is just right"
        if the temperature is between 61 and 99 inclusive.
        The program continues to ask for temperatures, and
        evaluates them as above, until the user enters a
        temperature of 0.
"""
def enter():
    return int(input("Enter a temperature: "))

temp = enter()

while temp != 0:
    if temp > 100:
        print("It is hot.")
    elif temp < 60:
        print("Its is cold.")
        print("It is just right.")
    elif temp > 60 and temp < 100:
        print("It is just right.")

    temp = enter()

print("Good bye!")
