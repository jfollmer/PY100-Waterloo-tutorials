# https://cscircles.cemc.uwaterloo.ca/16-recursion/

# First time doing this exercise (I think).
# This exercise follows the "Digital Sum" exercise and its variation.

"""
Short Answer Exercise: GCD

What is the output of the following recursive program?

This remarkably short program computes the greatest common divisor of 
two numbers. This is known as the Euclidean Algorithm, one of the oldest 
known algorithms (https://en.wikipedia.org/wiki/Euclidean_algorithm).
"""

def gcd(a, b): # a=20, b=12
    if b == 0:
        return a

    return gcd(b, a % b) # a=20, b=12, a%b==8 => a=12, b=8;
                         # a=12, b=8, a%b==4 => a=8, b=4;
                         # a=8, b=4, a%b==4 => a=4, b=4
                         # a=4, b=4, a%b==0 => 
                         # 4 is returned down the stack

print(gcd(20, 12)) # 4