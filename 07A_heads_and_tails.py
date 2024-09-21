# Waterloo tutorials, 7A. Strings, "Heads and Tails" exercise
# https://cscircles.cemc.uwaterloo.ca/7a-strings/

"""Write a program which reads a string using input(), and outputs the 
same string but with the first and last character exchanged. (You may 
assume the input string has length at least 2.) For example, on input 
Fairy a correct program will print yairF.
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

inputs = [
    'meat',              # team
    'yo',                # oy
    'same words',        # same words
    'hkhpggkovj',        # jkhpggkovh
    'xlajkrpsjlcwa',     # alajkrpsjlcwx
    'rvcofliaegrqkvyuk', # kvcofliaegrqkvyur
]

# string = input() # replaced with the inputs list and iterating over it
for string in inputs:
    # the solution I used on the website:
    print(string[-1] + string[1:len(string) - 1] + string[0])