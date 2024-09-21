# https://cscircles.cemc.uwaterloo.ca/15b-python-pushups/

# I redid this and added it here after completing PY101. The solution I 
# came up with the first time through is at the very bottom. I tried to 
# solve it without using techniques I didn't know about then.

"""
Coding Exercise: Credit Check

You have been hired by MeisterCard to write a function which checks 
if a given credit card number is valid. Your function check(S) should 
take a string S as input. First, if the string does not follow the 
format "#### #### #### ####" where each # is a digit, then it should 
return False. Then, if the sum of the digits is divisible by 10 (a 
"checksum" method), then the procedure should return True, else it 
should return False. For example, if S is the string 
"9384 3495 3297 0123" then although the format is correct, the digit 
sum is 72 so you should return False.
"""

inputs = [
    ('2768 3424 2345 2358', False),
    ('9384 3495 3297 0121', True),
    ('0000000000000000', False),
    ('1876 0954 325009182', False),
    (' 5555 5555 5555 5555', False),
    ('0000 0000 0000 000', False),
    ('0 0 0 0000000000000', False),
    ('', False),
    ('0000 0000', False),
    ('0123 4567 8902 4568', True),
    ('0123 4567 89AB EFGH', False),
    ('0000 000000000000', False),
    ('93841 3495 3297 012', False),
]

def check(S):
    if len(S) != 19:
        return False
   
    S = S.split()
    digit_sum = 0
   
    for section in S:
        if len(section) != 4 or section.isdigit() == False:
            return False

        for digit in section:
            digit_sum += int(digit)
   
    if digit_sum % 10 != 0:
        return False
   
    return True

for number, correct_result in inputs:
    print(check(number), correct_result)


# original solution:

# def check(S):
#     if len(S) != 19: return False # check format for length
#     for i in range(4, len(S), 5): # check format: return False if every 5th character isn't a space
#         if S[i] != ' ': return False

#     List = list() # initialize a list to put the digits of S in to do math on
#     sum = 0 # start checksum
#     for char in S: 
#         if char != ' ': # create a list without the spaces
#             List = List + [char]
#             if char.isdigit() == False:
#                 print("False line 11")
#                 return False
#             else:
#                 sum = sum + int(char)
#     print(sum)
#     print(List)
    
#     if sum % 10 != 0:
#         print("False")
#         return False
#     if sum % 10 == 0:
#         print("True")
#         return True

# check('2768 3424 2345 2558')

# some random testing I guess I was doing, kept so I can look back on
# my thought process later:

# List = [1, 'a', 'b', 'c']
# for x in List:
#     if List[list.index(x)].isdigit() == False: print("False")

# check('4949 5678 0123 4675')