# Waterloo tutorials, 7A. Strings, "Next Letter" exercise
# https://cscircles.cemc.uwaterloo.ca/7a-strings/

"""Write a program that takes a character as input (a string of length 
1), which you should assume is an upper-case character; the output 
should be the next character in the alphabet. If the input is 'Z', your 
output should be 'A'. 
"""

inputs = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# char = input() # replaced with inputs list and iterating over it
                 # could replace it with random selections but that 
                 # seems like overkill
for char in inputs:
    # the solution I used on the website:
    if ord(char) < 90:
        print(chr(ord(char) + 1))
    elif ord(char) == 90:
        print(chr(ord(char) - 25))