# https://cscircles.cemc.uwaterloo.ca/16-recursion/

# First time reading/doing this exercise.
# This follows the "Searching a Nested List" exercise.

"""
This Rules

Recursion is also related to fractals — images which contain multiple 
smaller copies of themselves. The banner at the top of this webpage is 
one example. The next exercise creates a simple repeating pattern using 
recursion.

Scramble Exercise: Fractal Ruler

Unscramble the lines to create a program that produces a recursive 
ruler-like design:

        else:
            ruler(n - 1)
        if n == 1:
            print('-')
            print(n * '-')
            ruler(n - 1)
    def ruler(n):

For example, when n=3 the program should output the 
following design:

    -
    --
    -
    ---
    -
    --
    -
"""

inputs = [3, 5]

def ruler(n):
    if n == 1:
        print('-')
    else:
        ruler(n - 1)
        print(n * '-')
        ruler(n - 1)

for num in inputs:
    ruler(num)