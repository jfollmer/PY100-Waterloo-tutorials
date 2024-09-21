# Waterloo tutorials, 7C. Loops, "Square Census" exercise
# https://cscircles.cemc.uwaterloo.ca/7c-loops/

"""The square numbers are the integers of the form K × K, e.g. 9 is a 
square number since 3 × 3 = 9. Write a program that reads an integer n 
from input and outputs all the positive square numbers less than n, one 
per line in increasing order. For example, if the input is 16, then the 
correct output would be
    1
    4
    9
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

inputs = [49, 59, 36, 63, 72, 64, 52, 43]

# n = int(inputs) # replaced with the inputs list and iterating over it
for n in inputs:
    n = int(n)
    # the solution I used on the website:
    for i in range(1, n):
        if i**2 < n:
            print(i**2)
    print() # extra line to divide outputs