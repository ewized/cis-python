Math Check
----------

Write an algorithm that determines whether a number is between 2 and 20 and is divisible by 3.

> x < 20 ; x > 2 ; x % 3 == 0

``` python
number = int(input("Enter a number"))

if number > 2 and number < 20 and number % 3 == 0:
    print(str(number) + " is between 2 - 20 and divisible by 3.")

```