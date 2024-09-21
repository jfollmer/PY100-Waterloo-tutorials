# https://cscircles.cemc.uwaterloo.ca/15b-python-pushups/

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.

"""
Suppose you have n flavours of ice cream, and want to make a sundae 
using exactly k of those flavours. How many different flavour 
combinations are possible? For example, if n=4 and k=2, there are 6 
possibilities:

(1) A and B, (2) A and C, (3) A and D, (4) B and C, (5) B and D, (6) C and D.

(for example here the flavours are Apricot, Blueberry, Chocolate, and Date).

Similarly, you could be choosing 2 people out of 4 (Al, Bob, Carol, Di) 
to make a committee. How many ways can the committee be built? The 
answer would still be 6. The next problem is about computing this 
number.

Coding Exercise: Be Choosy

The number of combinations of k things out of a total of n things is 
equal to

    n/k * (n-1)/(k-1) * (n-2)/(k-2) * ... * (n-k+2)/2 * (n-k+1)/1

Write a function choose(n, k) which takes two integers n and k; we 
guarantee n>k>0. The function should return the value given in the 
formula above.

Note that for this exercise, we expect you to just mechanically compute 
this formula without trying to understand it. But if you're interested, 
here's a sample YouTube video explaining it:
https://youtu.be/w1nlzDAVyzk?t=313
"""

inputs = [(4, 2), (7, 3), (10, 1), (16, 7), (18, 6)]

def choose(n, k):
    result = n / k

    while k > 1:
        result *= (n - 1) / (k - 1)
        n -= 1
        k -= 1

    return result

for n, k in inputs:
    print(choose(n, k))