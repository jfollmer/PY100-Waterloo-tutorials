# Waterloo tutorials, 7B. Math, "Divisibility" exercise
# https://cscircles.cemc.uwaterloo.ca/7b-math/

"""
Write a program that reads two positive integers a and b on separate 
lines. If a is divisible by b, print the message "divisible". Otherwise, 
print the message "not divisible". For example, when the input is
    14
    3
the program should print "not divisible".
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

inputs = [
    (14, 3),
    (18, 4),
    (24, 6),
    (6, 2),
    (6, 4),
    (102, 3),
    (100, 3),
]

# a = int(input()) # replaced with the inputs list and iterating over it
# b = int(input())
for (a, b) in inputs:
    # the solution I used on the website:
    if a % b == 0:
        print('divisible')
    else:
        print('not divisible')