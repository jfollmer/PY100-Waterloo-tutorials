# https://cscircles.cemc.uwaterloo.ca/16-recursion/

# I redid this after completing PY101. Previously, I got this working 
# sort of by accident, and I semi-understood it at the time. This time 
# I understood it better.

"""
Here is a program that uses recursion to achieve the same effect as a 
`while` loop in the lesson on loops.

    def countdown(n):
        if n == 0:
            print('Blastoff!')
        else:
            print(n)
            countdown(n - 1)

    countdown(5)

Let's add some extra print statements to help us understand how the 
program works. This version of the program also reads the time limit 
from input.

    def countdown(n):
        print('Entering countdown(',n,')')
        if n == 0:
            print('Blastoff!')
        else:
            print(n)
            countdown(n - 1)
        print('Exiting from countdown(',n,')')

    limit = int(input())
    countdown(limit)

If you like, use Enter input with the above program to try other input 
values. Try 0 first and see what happens, and then 1.

When the input is 5, the program first calls a copy of the countdown 
function with n=5, which prints 5 and calls countdown(4). This continues 
until countdown(0), which prints "Blastoff!" and does not call countdown 
any more. When Python finishes executing the n=0 call of the countdown 
function, Python returned to the function that called it, which is the 
n=1 call of the countdown. Then we return to the n=2 call, and so on.

To double-check our understanding, we can also visualize the recursive 
code:
https://cscircles.cemc.uwaterloo.ca/visualize/#code=def%20countdown(n)%3A%0A%20%20if%20n%20%3D%3D%200%3A%0A%20%20%20%20print('Blastoff!')%0A%20%20else%3A%0A%20%20%20%20print(n)%0A%20%20%20%20countdown(n%20-%201)%0A%0Acountdown(5)

The new twist, which makes recursion unique from the functions we've 
seen before, is that multiple versions of the function are running at 
the same time. That is to say, there is more than one frame at a time 
corresponding to the same function. This is pretty much the same as what 
we saw in the visualization where one function called another, except 
now the calling function is the same as the function being called. 
However, you have to be careful to note that at each step, only the 
"current" variables (the newest/bottom-most frame) are really used — the 
non-bottom frames are "paused" and their variables inaccessible.

Modify the countdown function so that it counts up instead of down.

Coding Exercise: Blast Up

Write a recursive function countup(n) which prints 'Blastoff!' followed 
by the numbers 1 to n on separate lines.

Hint: Move the `print(n)` statement.

def countdown(n):
    if n == 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)


"""

inputs = [3, 9, 12, 8]

# this is the version I got working first:

def countup(n):
   if n > 0: # if n == 0 previously
      countup(n - 1) # difference between putting the call above or below print(n)
                     # makes a sort of flat then back downhill V shape
                     # vs downhill then flat coming back
      print(n)
   elif n == 0:
      print('Blastoff!')

for num in inputs:
    countup(num)

# this version also works and is closer to `countup(n)`:

def countup(n):                 # def countdown(n):
    if n == 0:                  #     if n == 0:
        print('Blastoff!')      #         print('Blastoff!')
    elif n > 0:                 #     else: # elif n > 0:
        countup(n - 1)          #         print(n)
        print(n)                #         countdown(n - 1)

for num in inputs:
    countup(num)

"""
Next, let's modify our countdown program to count in increments of 2. 
The output should be 5, 3, 1, Blastoff! We will change the function 
argument from n-1 to n-2. Is there anything else that we need to change?

    def countdownBy2(n):
        if n == 0:
            print('Blastoff!')
        else:
            print(n)
            countdownBy2(n - 2)

    countdownBy2(5)

You can see that this program did not work as we intended. It printed 
5, 3, 1, like we wanted, but instead of stopping it continued with 
-1, -3, -5 and ran forever. (More precisely, it runs out of time and 
memory, because each recursive call takes up a little more working 
memory; see the same example in the visualizer.)

When designing a recursive function, we must be careful that its 
sequence of calls does not continue forever! Modify the countdownBy2 
program above so that it correctly stops at 1 (or 2, if n is even) and 
prints 'Blastoff!'.

Coding Exercise: Double Time

Modify this recursive program to correctly count down in increments of 
2.

    def countdownBy2(n):
        if n == 0:
            print('Blastoff!')
        else:
            print(n)
            countdownBy2(n - 2)
    # delete this comment and enter your code here

"""

inputs = [10, 13, 14]

def countdownBy2(n):
    if n <= 0: # was == previously
        print('Blastoff!')
    else:
        print(n)
        countdownBy2(n - 2)

for num in inputs:
    countdownBy2(num)