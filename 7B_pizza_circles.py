# Waterloo tutorials, 7B. Math, "Pizza Circles" exercise
# https://cscircles.cemc.uwaterloo.ca/7b-math/

"""Your friends have eaten their square pizzas and are now ordering a 
round pizza. Write a program to calculate the area of this circular 
pizza. The input is a float r, which represents the radius in cm. The 
output should be the area in cm2, calculated using the formula  A=pi*r2. 
Use Python's pi feature instead of typing 3.1415...
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

from math import pi

inputs = [1.0, 31.9, 24.1]

# radius = float(input()) # replaced with the inputs list and iterating over it
for radius in inputs:
    # the solution I used on the website:
    area = pi * radius**2
    print(area)