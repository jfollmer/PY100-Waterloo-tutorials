# https://cscircles.cemc.uwaterloo.ca/9-else-and-or-not/

"""
The words 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th are called 
*ordinal adjectives*. Write a program which reads an integer x between 
1 and 9 from input. The program should output the ordinal adjective 
corresponding to x.
Hint: you don't need to have 9 separate cases; 4 is enough.
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

inputs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def ordinal(x):
    # x = input() # replaced with the inputs list and iterating over it
    if x == '1':
        print(x + 'st')
    elif x == '2':
        print(x + 'nd')
    elif x == '3':
        print(x + 'rd')
    else:
        print(x + 'th')

for num in inputs:
    ordinal(num)