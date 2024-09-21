# https://cscircles.cemc.uwaterloo.ca/14-methods/

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

"""
Coding Exercise: The Replacements
Using index and other list methods, write a function replace(list, X, Y) 
which replaces all occurrences of X in list with Y. For example, if 
L = [3, 1, 4, 1, 5, 9] then replace(L, 1, 7) would change the contents 
of L to [3, 7, 4, 7, 5, 9]. To make this exercise a challenge, you are 
not allowed to use []. 

Note: you don't need to use return.

Hint: Start with `while list.count(X) > 0:` or `while X in list:`.
"""

inputs = [
    ([3, 1, 4, 1, 5, 9], 1, 7),
    (['I', 'am', 'what', 'I', 'am'], 'am', 'was'),
    ([3], 1, 2),
]

# Solution before looking at hint:

def replace(L, X, Y):
    for element in L:
        if element == X:
            i = L.index(element)
            L.remove(element)
            L.insert(i, Y)

for L, X, Y in inputs:
    replace(L, X, Y)
    print(L)

# Solution after looking at hint:

def replace(list, X, Y):
   while X in list:
      i = list.index(X)
      list.remove(X)
      list.insert(i, Y)

for L, X, Y in inputs:
    replace(L, X, Y)
    print(L)