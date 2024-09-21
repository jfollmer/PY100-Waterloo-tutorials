# https://cscircles.cemc.uwaterloo.ca/16-recursion/

# First time doing this exercise. After doing the others, this was
# actually easy.

# This exercise follows the "GCD" exercise.

"""
Coding Exercise: Hailstone

The hailstone sequence starting at a positive integer n is generated by 
following two simple rules. If n is even, the next number in the 
sequence is n/2. If n is odd, the next number in the sequence is 3*n+1. 
Repeating this process, we generate the hailstone sequence. Write a 
recursive function hailstone(n) which prints the hailstone sequence 
beginning at n. Stop when the sequence reaches the number 1 (since 
otherwise, we would loop forever 1, 4, 2, 1, 4, 2, ...)

For example, when n=5, your program should output the following 
sequence:

    5
    16
    8
    4
    2
    1

Mathematicians believe that every hailstone sequence reaches 1 
eventually, no matter what value of n we start with. However, no one has 
been able to prove this yet.
"""

inputs = [5, 4, 21, 24, 124, 159]

def hailstone(n):
    if n == 1:
        print(n)
    elif n % 2 == 0:
        print(n)
        hailstone(n // 2)
    elif n % 2 == 1:
        print(n)
        hailstone(3 * n + 1)

for num in inputs:
    hailstone(num)
    print()