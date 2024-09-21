# https://cscircles.cemc.uwaterloo.ca/9-else-and-or-not/

"""
As an example of using and, here is a program which converts numbers to 
letters, with some error-checking.

x = int(input())
if x>=1 and x<=26:
    print('letter', x, 'in the alphabet:', chr(ord('A')+(x-1)))
else:
    print('invalid input:', x)

Write a program which does the reverse of the example above: it should 
take a character as input and output the corresponding number (between 
1 and 26). Your program should only accept *capital* letters. As error-
checking, print `invalid` if the input is not a capital letter.

"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

inputs = 'QY@[eVJ'

def alpha_order(letter):
    # letter = input() # replaced with inputs list and iterating over it
    if ord('A') <= ord(letter) <= ord('Z'):
        print(ord(letter) - ord('A') + 1)
    else:
        print('invalid')

for letter in inputs:
   alpha_order(letter)