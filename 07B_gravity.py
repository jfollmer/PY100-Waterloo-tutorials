# Waterloo tutorials, 7B. Math, "Gravity" exercise
# https://cscircles.cemc.uwaterloo.ca/7b-math/

"""A parcel is thrown downward at a speed of v m/s from an airplane at 
altitude 11000 m. As it falls, its distance from the ground is given by 
the formula -4.9t2 - vt + 11000, where t is the time in seconds since it 
was dropped. Write a program to output the time it will take to reach 
the ground. The input to your program is the positive floating-point 
number v. The required time is given by the quadratic formula
    (image of formula given here)
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

from math import sqrt

inputs = [1.0, 33.0, 25.9]

# v = float(input()) # replaced with the inputs list and iterating over it
for v in inputs:
    # the solution I used on the website:
    numerator = v - sqrt(v**2 - (4 * (-4.9) * 11000))
    denominator = 2 * (-4.9)
    print(numerator / denominator)