# Waterloo tutorials, 7A. Strings, "Pig Latin" exercise
# https://cscircles.cemc.uwaterloo.ca/7a-strings/

"""Pig Latin is a nonsense language. To transform a word from English to 
Pig Latin, you move the first letter to the end and add "ay" after that. 
For example, monkey becomes onkeymay in Pig Latin, and word becomes 
ordway. Write a program that takes a single word as input and translates 
it to Pig Latin. (In reality, Pig Latin has rules that are more complex 
than this, but we ignore them for the purposes of this exercise.)
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

inputs = [
    'funky', # unkyfay
    'potato', # otatopay
    'human', # umanhay
    'purple', # urplepay   
]

# word = input() # replaced with the inputs list and iterating over it
for word in inputs:
    # the solution I used on the website:
    print(word[1:len(word)] + word[0] + 'ay')