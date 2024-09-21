# https://cscircles.cemc.uwaterloo.ca/16-recursion/

# First time reading/doing this exercise.
# This follows the "Hailstone" exercise.

"""
Nested Lists

Here is an interesting natural application of recursion. A nested list 
is one where you put some lists inside of others, possibly multiple 
times. For example, some nested lists of integers are [[1, 2], [9, 10]] 
as well as [[1], 2] and x = [[1], 2, [3, [[4]]]]. The last nested list 
example is a list with three elements: x[0]==[1] to begin, then x[1]==2, 
then x[2]==[3, [[4]]]. (So x, viewed as a list, has length 3). Note that 
a list like [1, 2, 3] also counts as a nested list. Can we write a 
function to find the total sum of any nested list of integers? For 
example, on input [[5], 2, [10, 8, [[7]]]] it should return the value 
32.

This task is difficult for a while loop or a for loop, since we want a 
function that works on nested lists with any shape/format. However, 
nested lists have a naturally recursive structure: a nested list is a 
list each of whose items is either (a) an integer or (b) a nested list. 
And, once we compute the sum of each subpart of the main list, the total 
of those values is the overall sum. We can express this with the 
following code; it uses isinstance(x, int) which gives a boolean value 
telling us whether x has integer type (as opposed to a list).

Example: Summing a Nested List

Computing the sum of the elements in a nested list with a recursive 
function. Once you press Run you will see its value on some tests:
"""

# their example:

def nestedListSum(NL):
    if isinstance(NL, int):     # case (a): NL is an integer
        return NL               # base case

    sum = 0                     # case (b): NL is a list of nested lists
    for i in range(0, len(NL)): # add subsums from each part of the main list
        sum = sum + nestedListSum(NL[i])
    return sum                  # all done

print(nestedListSum([1, 2, 3]))               # 6
print(nestedListSum([[1, 10], [100, 10]]))    # 121
print(nestedListSum([[3], [[5, [4]], 2, 1]])) # 15
print(nestedListSum([[[[54238]]]]))           # 54238
print(nestedListSum([1, [2, [3, [4, [5]]]]])) # 15

# my slight rewrite for better understanding:

def nestedListSum(NL):
    if isinstance(NL, int):    # base case
        return NL
    elif isinstance(NL, list): # recursive case:
        sum = 0                # add subsums from each part of the main list
        for i in range(0, len(NL)):
            sum = sum + nestedListSum(NL[i])
        return sum

"""
Recursion is used to break down each nested list into smaller parts. For 
example, nestedListSum([1, [3, 4], 5]) makes a total of 6 recursive 
calls: the initial one, then on 1, then on [3, 4], then on 3, then 4, 
(after which the [3, 4] total is returned as 7) and finally on 5 (after 
which the overall total 13 is obtained). Here is the same code in the 
visualizer:
https://cscircles.cemc.uwaterloo.ca/visualize/#code=def%20nestedListSum(NL)%3A%0A%20%20%20%20if%20isinstance(NL%2C%20int)%3A%20%20%20%20%20%23%20case%20(a)%3A%20NL%20is%20an%20integer%0A%20%20%20%20%20%20%20%20return%20NL%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20base%20case%0A%0A%20%20%20%20sum%20%3D%200%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20case%20(b)%3A%20NL%20is%20a%20list%20of%20nested%20lists%0A%20%20%20%20for%20i%20in%20range(0%2C%20len(NL))%3A%20%23%20add%20subsums%20from%20each%20part%20of%20the%20main%20list%0A%20%20%20%20%20%20%20%20sum%20%3D%20sum%20%2B%20nestedListSum(NL%5Bi%5D)%0A%20%20%20%20return%20sum%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20all%20done

Coding Exercise: Searching a Nested List

By writing something similar to nestedListSum, define a recursive 
function

    nestedListContains(NL, target)

that takes a nested list NL of integers and an integer target, and 
indicates whether target is contained anywhere in the nested list. Your 
code should return the boolean value True when it is contained in the 
nested list, and False if it is not contained in it.

For example, nestedListContains([1, [2, [3], 4]], 3) should give True 
and nestedListContains([1, [2, [3], 4]], 5) should give False.
"""

inputs = [
    ([2, 3, 5, 7, 9], 7),
    ([2, 3, 5, 7, 9], 8),
    ([[9, 4, 5], [3, 8]], 3),
    ([[9, 4, 5], [3, 8]], 6),
    ([[[[[[[5]]]], 4]]], 3),
    ([[[[[[[7]]]], 8]]], 7),
    ([3, 7, [5], 9], 7),
]

def nestedListContains(NL, target):
   if type(NL) == int and NL == target:
      return True
   elif type(NL) == list:
      for i in range(len(NL)):
         if nestedListContains(NL[i], target):
            return True
   return False

print()
for lst, target in inputs:
    print(nestedListContains(lst, target))