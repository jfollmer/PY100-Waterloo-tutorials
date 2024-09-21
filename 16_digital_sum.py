# https://cscircles.cemc.uwaterloo.ca/16-recursion/

# I redid this and added it here after completing PY101. I couldn't get
# it working before and gave up when told we didn't have to learn
# recursion yet. But I finally tried again and figured it out in the
# middle of the night.

# This exercise follows the "Blast Up" exercise and its variations.

"""
Designing recursive functions

A recursive function just means a function that calls itself. But there 
must be some occasions when the function does not call itself, or else 
the program will run forever, like we saw above. A base case is the part 
of a recursive function where it doesn't call itself. In the example 
above, the base case was n<=0. Designing a recursive function requires 
that you carefully choose a base case and make sure that every sequence 
of function calls eventually reaches a base case.

In the next exercise, the base case has been programmed for you, but you 
will write the rest of the recursive function.

Coding Exercise: Digital Sum

The digital sum of a number n is the sum of its digits. Write a 
recursive function digitalSum(n) that takes a positive integer n and 
returns its digital sum. For example, digitalSum(2019) should return 12 
because 2+0+1+9=12.

Hint #1: Remove one digit and use your `digitalSum` function to compute 
the sum of the remaining digits.

Hint #2: Use `n % 10` and `n // 10` to deal with one digit at a time.

    def digitalSum(n):
      if n < 10:
     return n
     else:
     # recursive case
    # delete this comment and enter your code here
"""

inputs = [2019, 9426, 930784, 3, 10, 10922]

# initial version with notes working it out:

def digitalSum(n):
   if n < 10:  # n == 2
      return n # and then 2 gets assigned to k
   elif n >= 10:
      k = digitalSum(n // 10) # 2019 -> 201, 201 -> 20, n=20 -> k=2 (then do math, 
                                                          # then return the sum)
      #k = n // 10 == 2
      #n % 10 == 0
      n = n % 10 + k #== 2
      return n # return 2 to 201, where n%10=1 + k=2 == 3
               # return 3 to 2019, where n%10=9 + k=3 == 12

for num in inputs:
    print(digitalSum(num))
print()

# clean version:

def digital_sum(n):
    if n < 10:
        return n
    elif n >= 10:
        k = digital_sum(n // 10)
        n = n % 10 + k
        return n

for num in inputs:
    print(digital_sum(num))
print()


# Previous version that I never got working:

# n = 2019

# def digitalSum(n):
#     if n < 10:
#         return n
#     else:
#         digitalSum(n // 10)
#     n = n % 10
#     return n

# digitalSum(n)

### This doesn't work yet.


"""
Now you will write a recursive function that calls digitalSum as a 
subroutine.

Coding Exercise: Digital Root

The digital root of a non-negative integer n is computed as follows. 
Begin by summing the digits of n. The digits of the resulting number are 
then summed, and this process is continued until a single-digit number 
is obtained. For example, the digital root of 2019 is 3 because 
2+0+1+9=12 and 1+2=3. Write a recursive function digitalRoot(n) which 
returns the digital root of n.

Assume that a working definition of digitalSum will be provided for your 
program.
"""

inputs = [9313, 805911, 288624, 1, 999999999999999, 
          8943918712468923447938, 99999999999199999999999,
          1364, 267104, 943540, 2, 2665, 590736, 412503, 6]

def digitalRoot(n):
    if n >= 10:
        n = digitalRoot(digitalSum(n))
        return n
    else:
        return n

for num in inputs:
    print(digitalRoot(num))
print()

# another version that works (just swapped if and else statements):
def digitalRoot(n):
    if n < 10:
        return n
    else:
        n = digitalRoot(digitalSum(n))
        return n

for num in inputs:
    print(digitalRoot(num))
print()

# seems like with the recursive call, you're essentially saying, "hey,
# test this again for some condition for me and get back to me when you 
# figure it out"