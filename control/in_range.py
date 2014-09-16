'''
name: Joshua Rodriguez
email: ewized@gmail.com
file: in_range.py
problem: chapter 2 number 7 page 145
description: Consider the Python function range(a, b).
    Label these statements as True or False.
    - The value "a" is included in the range.
    - The value "b" is included in the range.
'''
a_state = False
b_state = False

A_RANGE = 0
B_RANGE = 10

for i in range(A_RANGE, B_RANGE):
    if A_RANGE == i:
        a_state = True

    if B_RANGE == i:
        b_state = True

print("The sate of a_state is: " + str(a_state))
print("The sate of b_state is: " + str(b_state))