# https://cscircles.cemc.uwaterloo.ca/11c-geometry/

# I redid these and added them here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve them
# without using techniques I didn't know about then.

"""
11C: Geometry
-------------
Lesson 11 has three parts A, B, C which can be completed in any order.

In this exercise we will create four functions which perform geometric computations:

a function to compute the length of a right triangle's hypotenuse,
a function to compute the perimeter of a right triangle,
a function to compute the distance between two points in 2D,
and a function to compute the perimeter of an arbitrary triangle.


Hypotenuse
----------
A right triangle is shown in the picture at the right-hand side. By 
definition, one of the angles of a right triangle equals 90 degrees (a 
right angle). The triangle has three sides. The side opposite the right 
angle has a special name: it is called the hypotenuse.

As shown in the diagram, let a and b denote the length of the sides 
adjacent to the right angle, and let c denote the length of the 
hypotenuse. The famous Pythagorean Theorem tells us that

    a^2 + b^2 = c^2

In the first problem, your task is to convert this theorem into a 
function which, given a and b, computes the length of the hypotenuse.

Coding Exercise: Hypotenuse

Define a function `hypotenuse(a, b)` which returns the length of the 
hypotenuse c, if the other two sides have lengths a and b.

Hint: You will need to `import math` and call `math.sqrt()` on something.
"""

inputs = [(3, 4), (17, 14), (20, 11), (11, 19), (20, 17)]

import math

def hypotenuse(a, b):
   return math.sqrt(a * a + b * b)

for a, b in inputs:
   print(hypotenuse(a, b))


"""
Perimeter
---------
Recall that the perimeter of a triangle is the sum of the sides. So in 
the diagram above, the perimeter has length a+b+c. Your program should 
assume that a correct version of hypotenuse has already been defined 
(you don't need to copy it from the first box to the second).

Coding Exercise: The Triangles are Right

Using hypotenuse(a, b), define a function rightTrianglePerimeter(a, b) 
which returns the length of the perimeter in a right triangle whose 
non-hypotenuse sides have lengths a and b.
"""

def rightTrianglePerimeter(a, b):
   c = hypotenuse(a, b)
   return a + b + c

for a, b in inputs:
   print(rightTrianglePerimeter(a, b))


"""
Distance in 2 Dimensions
------------------------
To talk about points living in two dimensions, we specify them using two 
coordinates (the Cartesian coordinate system), the x coordinate and the 
y coordinate. We would like to write a function whose input is a pair of 
points, and whose output is the distance between those two points. It 
turns out that the hypotenuse function helps us perform this task!

In more detail, let the first point have coordinates (x1, y1) where x1 
and y1 are real numbers, and let the second point have coordinates 
(x2, y2). The key idea is to draw the right triangle shown in the 
diagram below: the hypotenuse goes from (x1, y1) to (x2, y2) and so its 
length equals the distance between the two points.

To calculate the length of the hypotenuse, we need to compute the length 
of the other two sides of the triangle. This can be done using the 
definition of coordinates (see the diagram): the horizontal displacement 
is a = x1-x2 and the vertical displacement is b = y1-y2.

Coding Exercise: 2D Distance

Assume hypotenuse(a, b) has already been defined. Using it, define a 
function distance2D(x1, y1, x2, y2) which calculates the distance 
between the point (x1, y1) and the point (x2, y2).
"""

inputs = [(0, 0, 3, 4), (11, 11, 14, 10), (8, 15, 16, 5)]

def distance2D(x1, y1, x2, y2):
   a = x1 - x2
   b = y1 - y2
   return hypotenuse(a, b)

for x1, y1, x2, y2 in inputs:
   print(distance2D(x1, y1, x2, y2))

"""
Perimeter of Any Triangle
-------------------------
We now have the final exercise of this lesson. Remember that the 
perimeter is the sum of the three sides lengths of the triangle; and 
note that the side length is the same as the distance between two of the 
triangle's points.

Coding Exercise: Secure the Perimeter

Assume distance2D(x1, y1, x2, y2) has already been defined. Using it, 
define a function trianglePerimeter(xA, yA, xB, yB, xC, yC) which 
calculates the perimeter of a triangle whose three points are (xA, yA), 
(xB, yB) and (xC, yC).
"""

inputs = [
   (0, 0, 0, 3, 4, 0),
   (3, 4, 9, 19, 1, 13),
   (10, 17, 19, 19, 2, 1),
]

def trianglePerimeter(xA, yA, xB, yB, xC, yC):
   a = distance2D(xA, yA, xB, yB)
   b = distance2D(xB, yB, xC, yC)
   c = distance2D(xC, yC, xA, yA)
   return a + b + c

for xA, yA, xB, yB, xC, yC in inputs:
   print(trianglePerimeter(xA, yA, xB, yB, xC, yC))