# Waterloo tutorials, 7C. Loops, "One Triangle" exercise
# https://cscircles.cemc.uwaterloo.ca/7c-loops/

"""Example of a for loop inside another for loop:
This code prints a 5×5 square of ones.  
Note: when we multiply a number X by ten and add one, we're essentially 
putting an extra 1 digit at the end of X. For example, 
(1867*10)+1=18671.

Code:
    for i in range(0, 5):
        X = 0
        for j in range(0, 5):
            X = (X*10)+1
        print(X)

Output:
    11111
    11111
    11111
    11111
    11111

Exercise: Modify the previous program in two ways. First, instead of a 
square, make it draw a triangle shaped like this: ◤. Second, instead of 
always having 5 lines, it should take the desired size as input from 
input(). For example, if the input is 3, then the output should be
    111
    11
    1
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

inputs = [3, 6, 9]

# n = int(input()) # replaced with the inputs list and iterating over it
for n in inputs:
    # the solution I used on the website:
    for i in range(1, n + 1):
        X = 0
        n -= 1
        for j in range(0, n + 1):
            X = (X*10)+1 # X =1, 11, 111, 1111, 11111
        print(X)         # X = 11111

# an entirely easier solution that doesn't use math but produces the 
# same result:
for n in inputs:
    for i in range(n, 0, -1):
        print(int('1' * i))