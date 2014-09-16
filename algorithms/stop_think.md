Stop and Think
--------------

When you are stuck on creating a program, it helps to stop and think.
Can you see what is wrong with the following program?
Why is it generating an error?

``` python
A_int = input("Enter an integer greater than 10: ")
    while A_int > 10:
    A_int = A_int - 1
    print(A_int)
```

The code has two problems:
1. The spacing was off on the while loop.
2. print() only works with strings, you must cast the int as a string.

``` python
A_int = input("Enter an integer greater than 10: ")
while A_int > 10:
    A_int = A_int - 1
    print(str(A_int))
```