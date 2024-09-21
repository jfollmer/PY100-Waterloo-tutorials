# https://cscircles.cemc.uwaterloo.ca/10-def/

# I redid these and added them here after completing PY101. Not sure what
# solutions I came up with the first time through. I tried to solve them
# without using techniques I didn't know about then.

"""
Define a function cube(n), which takes a single number n as input, and 
outputs its cube n × n × n.
"""

inputs = [10, 11, 8, 1.26]

def cube(n):
   return n**3

for num in inputs:
   print(cube(num))


"""
Define a function rectanglePerimeter(width, height) that returns the 
perimeter of a rectangle.
"""

inputs = [(3, 4), (57, 18), (22.125, 84.25)]

def rectanglePerimeter(width, height):
   return width * 2 + height * 2

for width, height in inputs:
   print(rectanglePerimeter(width, height))