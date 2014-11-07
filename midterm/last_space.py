'''
name: Joshua Rodriguez
email: ewized@gmail.com
file: last_space.py
problem: Midterm #2
description: Demonstrate how you would find the last space in a string.
'''

string = "The last space in a string."
count = 1;

for char in string[::-1]:
    if char == ' ':
        break;

    count += 1

index = len(string) - count

print("The char at the index:", string[index])
print("The index of the last space:", index)
