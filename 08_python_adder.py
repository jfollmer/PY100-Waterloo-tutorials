# Waterloo tutorials, 8. Remix, "Python Adder" exercise
# https://cscircles.cemc.uwaterloo.ca/8-remix/

"""Write a program that takes a single input line of the form 
«number1»+«number2», where both of these represent positive integers, 
and outputs the sum of the two numbers. For example on input 5+12 the 
output should be 17.
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

inputs = [
    '10542+823093799',      # 823104341
    '693+86457',            # 87150
    '848319344+15146',      # 848334490
    '8234708+258148',       # 8492856
    '465705864+1963566795', # 2429272659
    '6506+10',              # 6516
    '1124+192',             # 1316
    '905689174+91268381',   # 996957555
    '26+749598',            # 749624
    '8682+852786647',       # 852795329
    '1899+13774',           # 15673
    '93981+700',            # 94681
    '10+42',                # 52
    '5228420+66464646',     # 71693066
    '53466416+153081751',   # 206548167
]

# S = input() # replaced with the inputs list and iterating over it
for string in inputs:
    # the solution I used on the website:
    for i in range(0, len(string)):
        if string[i] == '+':
            plus = i
    num1 = int(string[0:plus])
    num2 = int(string[plus+1:len(string)])
    print(num1 + num2, num1, num2)