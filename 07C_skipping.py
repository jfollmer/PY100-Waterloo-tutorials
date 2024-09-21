# Waterloo tutorials, 7C. Loops, "Skipping" exercise
# https://cscircles.cemc.uwaterloo.ca/7c-loops/

"""Extend the "Looping through all lines of input" example above 
(we've copied it for you) by adding a new feature: any line equal to 
SKIP should not be printed, and should not cause the counter to be 
increased. Run the program to see an example.

Program:
    counter = 0
    while True:
        lineIn = input()
        if lineIn=='END':
            break
        counter = counter+1
        print('line', counter, '=', lineIn)
Input:
    fish
    dog
    SKIP
    cat
    END
    bear
Output:
    line 1 = fish
    line 2 = dog
    line 3 = SKIP
    line 4 = cat
Expected this correct output:
    line 1 = fish
    line 2 = dog
    line 3 = cat
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

inputs = [
    [
        'fish',
        'dog',
        'SKIP',
        'cat',
        'END',
        'bear',
    ],
    [
        'SKIP',
        'flip',
        'drip',
        'END',
        'END',
    ],
    [
        'the next line is blank but important',
        '',
        'SKIP',
        'SKIP',
        'SKIP',
        'to my loo',
        'END',
    ],
]

# My adjustment (do not run this code, endless loop, can't immediately
# figure out how to make it iterate through inputs while still using a 
# while loop):

# counter = 0
# while True:
#     lineIn = input()
#     if lineIn == 'SKIP':
#         continue
#     if lineIn=='END':
#         break
#     counter = counter+1
#     print('line', counter, '=', lineIn)

# My adjustments just to make it iterate through inputs list:

for lines in inputs:
    counter = 0
    for line in lines:
        if line == 'SKIP':
            continue
        if line == 'END':
            break
        counter = counter + 1
        print('line', counter, '=', line)
    print() # blank line to separate outputs