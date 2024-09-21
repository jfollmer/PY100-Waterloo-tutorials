

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.


















# The digital sum of a number n is the sum of its digits. 
# Write a recursive function digitalSum(n) that takes a positive integer n and returns its digital sum. 
# For example, digitalSum(2019) should return 12 because 2+0+1+9=12.

n = 2019

def digitalSum(n):
    if n < 10:
        return n
    else:
        digitalSum(n // 10)
    n = n % 10
    return n

degitalSum(n)

### This doesn't work yet.
### https://cscircles.cemc.uwaterloo.ca/16-recursion/