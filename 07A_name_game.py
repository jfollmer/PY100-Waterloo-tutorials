# Waterloo tutorials, 7A. Strings, "Name Game" exercise
# https://cscircles.cemc.uwaterloo.ca/7a-strings/

"""The Name Game lets you make a song out of any person's name. Listen 
to the song to get an idea of how it works:


Your program should take a person's name as input, for example "pearl," 
and print out the song like
    pearl, pearl, bo-bearl
    banana-fana fo-fearl
    fee-fi-mo-mearl
    pearl!
Note that the entire name appears three times; in addition the name 
appears three more times with the first letter replaced by b, f, or m. 
(In reality, the song has rules that are more complex than this, but we 
ignore them for the purposes of this exercise.)
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

inputs = ['jimmy', 'pauline', 'aaron', 'sara']

# name = input() # replaced with the inputs list and iterating over it
for name in inputs:
    # the solution I used on the website:
    suffix = name[1:len(name)]
    print(name + ', ' + name + ', ' + 'bo-b' + suffix)
    print('banana-fana fo-f' + suffix)
    print('fee-fi-mo-m' + suffix)
    print(name + '!')
    print() # extra line to divide outputs