# https://cscircles.cemc.uwaterloo.ca/14-methods/

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

"""
Coding Exercise: Exact Postage

Define a function postalValidate(S) which first checks if S represents 
a postal code which is valid:
    * first, delete all spaces;
    * the remainder must be of the form L#L#L# where L are letters (in 
      either lower or upper case) and # are numbers.
If S is not a valid postal code, return the boolean False. If S is 
valid, return a version of the same postal code in the nice format 
L#L#L# where each L is capital.
"""

inputs = ['H0H0H0', 'postal', '  d3  L3  T3', '  3d3  L3  T', '',
          'n2l 3g1z', 'V4L1D?', 'K1A 0A3', 'H0H0H']

def postalValidate(S):
    S = S.replace(' ', '')
    if not len(S) == 6:
        return False
    if not S[0::2].isalpha():
        return False
    if not S[1::2].isdigit():
        return False
    return S.upper()

for S in inputs:
    print(postalValidate(S))

# I honestly have no idea how I solved this the first time without 
# knowing about the str.replace(' ', '') trick, or ''.join(list). I
# must have looked at the documentation since this lesson links to it,
# or just googled the answer, or skipped it.