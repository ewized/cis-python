1.

monty = "Monty Python"

print(monty[:1])
print(monty[-1:])
print(monty[len(monty) - 1:])
print(monty[0:5])

-----------------------------------------

2.

homebody = "homebody"

print(homebody[:4])
print(homebody[4:])

-----------------------------------------

3.

S = "Year4000"

size = int(len(S))
half = int(size / 2)

print(S[:half])
print(S[half:size])

-----------------------------------------

4.

S="I had a cat named amanda when I was little"
count = 0
iterable = 0

while iterable < len(S):
    
    if S[iterable] == 'a':
        count += 1

    iterable += 1

print(str(count))

-----------------------------------------

5.

# The reason is the space counts as an input
first, space, second = input("two spaced-separated numbers: ")

print(first, " ", second)

-----------------------------------------

6.

print("Line one \nLine two")

-----------------------------------------

7.

s1, s2, s3, s4 = "concord", "souix city", "HONOLULU", "TopHat"

# a, will make the first char uppercase
print("Capitalize:", s1.capitalize())

# b, will make the first char of each word uppercase
print("Title:", s2.title())

# c, will switch each lowercase char to uppercase and visa versa
print("Swapcase:", s4.swapcase())

# d, will make the letters uppercase
print("Upper:", s1.upper())

# e, will make the letters lowercase
print("Lower:", s3.lower())

-----------------------------------------

8.

string = "Year4000 Network | mc.year4000.net"

# Counts the number of e's in the String
print("Counting `e`:", string.count("e"))

# Counts the number of 0's in the string
print("Counting `0`:", string.count("0"))

-----------------------------------------

9.

line = "#"
for i in range(1, 80):
    line += "#"

print(str(line))
# Debug test the length of the string
# print(len(line)

print("#\n" * 30)


-----------------------------------------

10.

string = "abcdefghij"

print(string[::-1], string[::3], string[-2::-2])