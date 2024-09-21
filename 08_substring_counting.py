# Waterloo tutorials, 8. Remix, "Substring Counting" exercise
# https://cscircles.cemc.uwaterloo.ca/8-remix/

"""As mentioned in lesson 7A, a substring is any consecutive sequence of 
characters inside another string. The same substring may occur several 
times inside the same string: for example "assesses" has the substring 
"sses" 2 times, and "trans-Panamanian banana" has the substring "an" 6 
times. Write a program that takes two lines of input, we call the first 
needle and the second haystack. Print the number of times that needle 
occurs as a substring of haystack.
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

inputs = {
    'needle': 'haystack', # 0
    'sses': 'assesses',  # 2
    'an': 'trans-Panamanian banana', # 6
    'o': 'pneumonoultramicroscopicsilicovolcanoconiosis', # 9
    '!!!': '!!!!!', # 3
}

# needle = input() # replaced with the inputs dictionary and iterating over it
# haystack = input()
for needle, haystack in inputs.items():
    # the solution I used on the website:
    i = 0
    count = 0
    for char in haystack:
        if len(needle) + i <= len(haystack):
            if haystack[i:len(needle) + i] == needle:
                count += 1
        i += 1
    print(count)

# Now that I know about the str.count(substr) method, it still doesn't
# work here because it only counts non-overlapping occurrences of the
# substring, not all occurrences including overlapping ones.