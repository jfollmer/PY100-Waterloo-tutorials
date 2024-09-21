# https://cscircles.cemc.uwaterloo.ca/13-lists/

# I redid these and added them here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve them
# without using techniques I didn't know about then.

"""
Coding Exercise: Monkey in the Middle

Write a function middle(L) which takes a list L as its argument, and 
returns the item in the middle position of L. (In order that the middle 
is well-defined, you should assume that L has odd length.) For example, 
calling middle([8, 0, 100, 12, 1]) should return 100, since it is 
positioned exactly in the middle of the list.

"""

inputs = [
    [8, 0, 100, 12, 1],
    ['Left', 'Middle', 'Right'],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    ['forever alone'],
    'forever alone',
]

def middle(L):
    return L[len(L) // 2]

for L in inputs:
    print(middle(L))
print()


"""
To solve the next exercise, use one of the operators we just introduced, 
and a for loop.

Coding Exercise: It's Natural

Write a function naturalNumbers which takes a positive integer n as 
input, and returns a list [1, 2, ...] consisting of the first n natural 
numbers.
"""

inputs = [12, 20, 1]

def naturalNumbers(n):
    numbers = []
    for i in range(1, n + 1):
        numbers += [i]
    return numbers

for n in inputs:
    print(naturalNumbers(n))
print()

"""
End of the Line: Negative Indices

To get the last item of a list, use

    «listName»[-1]

More generally, L[-k] returns the kth item from the end of the list; 
Python handles this internally by translating it to L[len(L)-k]. This 
shortcut notation works for strings too!

Coding Exercise: Palindrome

A palindrome is a word which is spelled the same forwards as backwards. 
For example, the word
    racecar
is a palindrome: the first and last letters are the same (r), the second 
and second-last letters are the same (a), etc. Write a function 
isPalindrome(S) which takes a string S as input, and returns True if the 
string is a palindrome, and False otherwise.
"""

inputs = ['racecar', 'ferrari', 'foolproof', 'cool', 'redder', 'pinker',
          'o', 'ok', 'kk', 'j0$Eog', 'rB#QzzQ#Br', 'y!I#r#I!y']

def isPalindrome(S):
    for i in range(len(S)//2):
        if S[i] != S[-i-1]:
            return False
    return True

for S in inputs:
    print(isPalindrome(S))
print()

"""
Coding Exercise: Product

Define a function prod(L) which returns the product of the elements in a 
list L.
"""

inputs = [
    [1, 2, 3, 4],
    [2, 2, 2, 2],
    [3, -1, 4, -1, -5],
    [3, 0, 9, 8, 1],
    [9, 1, 7],
    [3, 2, 4],
]

def prod(L):
    product = 1
    for i in range(len(L)):
        product *= L[i]
    return product

for L in inputs:
    print(prod(L))
print()

"""
Looping through lists

It is very common (like in the previous exercise) to loop through every 
value in a list. Python allows a shortcut to perform this type of an 
operation, usually called a "for all" loop or a "for each" loop. 
Specifically, when L is a list, this code

  for x in L:
    «loop body block»
  
does the following: first x is set to the first value in L and the body 
is executed; then x is set to the second value in L and the body is 
executed; this is continued for all items in L.

Coding Exercise: for in

Define the function prod(L) as before, but this time using the new kind 
of loop.
"""

def prod(L):
    product = 1
    for num in L:
        product *= num
    return product

for L in inputs:
    print(prod(L))
print()

"""
Short Answer Exercise: Mystery Function

What is the value of x which will cause mystery(x) to run forever?

def mystery(x):
  a = [0, 4, 0, 3, 2]
  while x > 0:
    x = a[x]
  return "Done"
"""

# answer: 3


"""
Scramble Exercise: à la Mode

The mode of a list is the element which occurs most frequently (the one 
which appears the maximum number of times). Unscramble the following 
program so that mode(L) correctly finds the mode, assuming L is a list 
of numbers from 0 to 9. (On our tests, there won't be two numbers tied 
for the maximum frequency.)

  for i in L:
      return i
  for i in range(0, 10):
    if frequency[i]==max(frequency):
def mode(L):
  frequency = [0]*10
    frequency[i] = frequency[i] + 1
"""

inputs = [
    [9, 6, 7, 1, 1, 1, 1],
    [4, 6, 2, 4, 7, 8, 3, 5, 6, 4, 5, 0],
]

def mode(L):
    frequency = [0] * 10
    for i in L:
        frequency[i] = frequency[i] + 1
    for i in range(0, 10):
        if frequency[i] == max(frequency):
            return i

for L in inputs:
    print(mode(L))