# Waterloo tutorials, 7B. Math, "Eggsactly" exercise
# https://cscircles.cemc.uwaterloo.ca/7b-math/

"""Egg cartons each hold exactly 12 eggs. Write a program which reads an 
integer number of eggs from input(), then prints out two numbers: how 
many cartons can be filled by these eggs, and how many eggs will be left 
over. For example, the output corresponding to 27 eggs is
    2
    3
since 27 eggs fill 2 cartons, leaving 3 eggs left over.
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

inputs = [25, 12, 10, 22]

# eggs = int(input()) # replaced with the inputs list and iterating over it
for eggs in inputs:
    # the solution I used on the website:
    cartons = eggs // 12
    leftovers = eggs % 12
    print(cartons)
    print(leftovers)
    print() # extra line to divide outputs