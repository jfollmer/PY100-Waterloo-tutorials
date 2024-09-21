# Waterloo tutorials, 8. Remix, "Watch the Pendulum" exercise
# https://cscircles.cemc.uwaterloo.ca/8-remix/

"""In physics, for a pendulum with length L and initial angle A, its 
horizontal displacement X(T) at time T is given by the formula:

X(T) = L × cos(A × cos(T × √9.8/L)) - L × cos(A)

Write a program which takes two lines of input; the first line is L and 
the second line is A. The output should be ten lines, giving the values 
of X(0), X(1), X(2), ..., X(9).

For example, if the first line of input is 53.1 and the second line of 
input is 0.8, then the first line of output is 0.0 and the second line 
of output is 53.1*cos(0.8*cos(1*√9.8/53.1)) - 53.1*cos(0.8) ~ 2.6689.
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.


"""Correct output for first set of inputs:
0.0
2.66890704872268
9.021742145820767
14.79454255758121
15.737746783283434
11.12490383561012
4.42369360407254
0.2737737560124529
1.295906539090339
6.8633099963334985
***
*********
***************
****************
***********
****

*
*******
"""

"""for second set:
0.0
6.092155526881907
7.564688684844054
0.21993433177204225
4.481065983288232
8.677048829284482
0.8701891992337419
2.941071405203923
9.24430249105672
1.9168262485354073
******
********

****
*********
*
***
*********
**
"""

"""for third set:
0.0
0.752121327716992
2.8775486702471937
6.003747657544324
9.576044463211844
12.950877666619675
15.510796304448405
16.78135861062077
16.52514699077335
14.790140424262148
*
***
******
**********
*************
****************
*****************
*****************
***************
"""

from math import sqrt
from math import cos

inputs = {
    53.1: 0.8,
    10: 1.5,
    213.7: 0.4,

}

# L = float(input()) # replaced with the inputs dictionary and iterating over it
# A = float(input())
for L, A in inputs.items():
    # the solution I used on the website:
    for i in range(10):
        displacement = L * cos( A * cos(i * sqrt(9.8/L)) ) - L * cos(A)
        print(displacement)
    print() # extra line to divide outputs