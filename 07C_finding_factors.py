# Waterloo tutorials, 7C. Loops, "Finding Factors" exercise
# https://cscircles.cemc.uwaterloo.ca/7c-loops/

"""If a × b = n, we call a × b a factorization of n. In this exercise, 
write a program that takes a positive integer n from input, and then 
outputs all factorizations of n; you should follow the formatting given 
by the following example for n=10.
    1 times 10 equals 10
    2 times 5 equals 10
    5 times 2 equals 10
    10 times 1 equals 10
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

inputs = [10, 8, 7, 30]

# n = int(input()) # replaced with the inputs list and iterating over it
for n in inputs:
    # the solution I used on the website:
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, 'times', str(n // i), 'equals', n)
    print() # blank line to separate outputs