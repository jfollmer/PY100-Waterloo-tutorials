# https://cscircles.cemc.uwaterloo.ca/15a-basic/

# I redid this and added it here after completing PY101. The solution I 
# came up with the first time through is at the very bottom. I tried to 
# solve it without using techniques I didn't know about then.

"""
The old programming language BASIC was famous for its numbered lines and 
goto statements. For this exercise, you will implement a simple version 
of BASIC with just these features. Specifically, the input to your 
program will consist of several lines in the format

    «label» goto «target»

where «label» and «target» are positive integers. The label is like the 
name or address of the line; all labels are unique. The target tells you 
the label of the line to move to next. The last line of the program is 
«label» END indicating that you should stop once you move to this line. 
Here is a sample BASIC program:

    5 GOTO 30
    10 GOTO 20
    20 GOTO 10
    30 GOTO 40
    40 END

When BASIC runs the program, this is what happens. We begin at the first 
line (with label 5). The line with label 5 has target 30, so next we go 
to the line with label 30. Then line 30 tells us to go to line 40. Line 
40 tells us to END. So, the program terminated successfully.

On the other hand, a BASIC program can also loop forever. Here is an 
example:

    10 GOTO 21
    21 GOTO 37
    37 GOTO 21
    40 END

The program starts at line 10, but then it loops forever between lines 
21 and 37.

Your task is to write a Python program, which reads a BASIC program as 
input. If the program terminates, your program should print success. If 
the program enters an infinite loop, your program should print infinite 
loop. Assume each target equals some valid label and that all labels are 
unique, so you do not have to do error-checking.

There are several ways you could do this, but in this lesson we have 
chosen one simple approach that breaks the problem in to 3 sub-tasks. 
(In lesson 15C you have one large problem and design the sub-tasks 
yourself.)


Sub-task 1: Reading the program
-------------------------------

To read the program, we need to keep calling input(). However, we need 
to stop calling input() once the last line (the one with END) is 
reached, to avoid an EOFError.

Coding Exercise: Reading the Program

Write a function getBASIC() which takes no arguments, and does the 
following: it should keep reading lines from input using a while loop; 
when it reaches the end it should return the whole program in the form 
of a list of strings. (Hints: about lists and stopping)
"""

inputs = [
    [
        '10 GOTO 20',
        '20 END'
    ],
    [
        '5 GOTO 30',
        '10 GOTO 20',
        '20 GOTO 10',
        '30 GOTO 40',
        '40 END',
    ],
    [
        '10 GOTO 21',
        '21 GOTO 37',
        '37 GOTO 21',
        '40 END',
    ]
]

def getBASIC(program):    # added argument as replacement
    lines = []

    i = 0                 # replacement
    while True:
        # line = input()  # replaced with lines marked "replacement"
        line = program[i] # replacement
        i += 1            # replacement
        lines.append(line)
        if 'END' in line:
            break

    return lines

for program in inputs:
   print(getBASIC(program))


"""
Sub-task 2: Go to it!
---------------------

Once we have read the program, we need to be able to move from line to 
line in the program. To accomplish this, we ask you to write the 
following subroutine.

Coding Exercise: Go to it!

Define a function findLine(prog, target) to perform the following. 
Assume prog is a list of strings containing a BASIC program, like the 
type generated by getBASIC(); assume target is a string containing a 
line number, which is the target of a GOTO statement. The function 
should return the index i (a number between 0 and len(prog)-1) such that 
prog[i] is the line whose label equals target.

Hint: You can use `split`.

Sample input/output: If you call

    findLine(['10 GOTO 20','20 END'], '10')

then the output should be 0, since item 0 of the list is the line with 
label 10.
"""

inputs = [
    (['10 GOTO 20', '20 END'], '20'),
    (['4 GOTO 12', '12 GOTO 99', '22 GOTO 22', '99 GOTO 12', '200 END'], '22'),
    (['10 GOTO 20', '20 END'], '10'),
    (['10 GOTO 100', '100 END'], '100'),
    (['10 GOTO 20', '15 GOTO 20', '20 END'], '20'),
    (['10 GOTO 100', '100 END'], '100'),
    (['10 GOTO 25', '15 GOTO 25', '20 GOTO 25', '25 END'], '25'),
]

def findLine(prog, target):
    for i in range(len(prog)):
        if prog[i].startswith(target):
            return i

for program, target in inputs:
   print(findLine(program, target))


"""
Sub-task 3: Smart Simulation
----------------------------

In the previous two exercises, we handled the input routine and the 
searching task. These will be useful to make writing the main program 
shorter. However, there is still a major question: how can we actually 
solve the original problem? The most straightforward way would be to 
simulate the BASIC program:

    * let prog be the BASIC program (an array of strings)
    * start a counter called location at 0, since we begin on the first 
      line of the program
    * while True,
        * if prog[location] is the END line, return "success" and stop.
        * let T be the target string indicated in prog[location]
        * let the new value of location be findLine(prog, T)

But, there is a major problem: this doesn't detect infinite loops, and 
if the BASIC program has an infinite loop, then the Python program will 
also loop forever. What we wanted was that the program should print 
"infinite loop" in this situation. We leave this problem for you to 
solve; we give a hint below.

Coding Exercise: Smart Simulation

Write a function execute(prog) to do the following. Assume prog is a 
list of strings containing the BASIC program, like before. Then, your 
function should return either "success" or "infinite loop" depending on 
whether the program terminates, or loops forever. Important: you should 
assume the procedure findLine(prog, target) defined in sub-task 2 is 
already defined, you do not need to re-write it.

Hint: ______________________

# here is a broken solution to get you started
def execute(prog):
  location = 0
  while True:
    if location==len(prog)-1: return "success"
    #get T from prog[location] via str.split
    location = findLine(prog, T)
"""

inputs = [
   ['10 GOTO 21', '21 GOTO 37', '37 GOTO 21', '40 END'],
   ['5 GOTO 30', '10 GOTO 20', '20 GOTO 10', '30 GOTO 40', '40 END'],
   ['10 GOTO 20', '20 END'],
   ['4 GOTO 12', '12 GOTO 99', '22 GOTO 22', '99 GOTO 12', '200 END'],
   ['10 GOTO 40', '20 GOTO 25', '25 GOTO 20', '40 END'],
]

def execute(prog):
   location = 0 # current location (index value)
   previous_locations = [0]

   while True:
      target = prog[location].split()[-1] # last element of current location
      location = findLine(prog, target)

      if location == len(prog) - 1:  # if location is last line, success
         return "success"
      elif location in previous_locations:
         return "infinite loop"
      else:
         previous_locations.append(location)

for program in inputs:
   print(execute(program))


"""
Putting it all together
-----------------------
To test your code as a complete solution, copy and paste your previous 
solutions into the following template.

    # def getBASIC from subtask 1

    # def findLine from subtask 2

    # def execute from subtask 3

    print(execute(getBASIC()))

"""

inputs = [
    [
        '10 GOTO 21',   
        '21 GOTO 37',
        '37 GOTO 21',
        '40 END',
    ], #infinite loop
    [
        '5 GOTO 30',
        '10 GOTO 20',
        '20 GOTO 10',
        '30 GOTO 40',
        '40 END',       
    ], # success
    [
        '10 GOTO 20',
        '20 END',
    ], # success
    [
        '4 GOTO 12',
        '12 GOTO 99',
        '22 GOTO 22',
        '99 GOTO 12',
        '200 END',
    ], # infinite loop
    [
        '10 GOTO 40',
        '20 GOTO 25',
        '25 GOTO 20',
        '40 END',
    ], # success
]

def getBASIC(program):    # added argument as replacement
    lines = []

    i = 0                 # replacement
    while True:
        # line = input()  # replaced with lines marked "replacement"
        line = program[i] # replacement
        i += 1            # replacement
        lines.append(line)
        if 'END' in line:
            break

    return lines

def findLine(prog, target):
    for i in range(len(prog)):
        if prog[i].startswith(target):
            return i

def execute(prog):
   location = 0 # current location (index value)
   previous_locations = [0]

   while True:
      target = prog[location].split()[-1] # last element of current location
      location = findLine(prog, target)

      if location == len(prog) - 1:  # if location is last line, success
         return "success"
      elif location in previous_locations:
         return "infinite loop"
      else:
         previous_locations.append(location)

# print(execute(getBASIC())) # replaced with loop below:
for program in inputs:
    print(execute(getBASIC(program)))



# original solution:

# def getBASIC():
#    prog = list()
#    while True:
#       line = input()
#       prog.append(line)
#       if line.endswith('END') == True:
#          return prog # return prog to print(execute(getBASIC()))

# def findLine(prog, target):
#    for line in prog:
#       Line = line.split()
#       if (Line[0]) == target:
#          return prog.index(line) # return location to execute() line 23

# def execute(prog):
#   location = 0
#   visited = [False] * len(prog)
#   while True:
#     if location==len(prog)-1: return "success"
#     else:
#        line = prog[location].split() # now have list of words
#        T = line[len(line)-1]
#     location = findLine(prog, T) # get new line number
#     if visited[location] == True:
#        return "infinite loop"
#     visited[location] = True

# print(execute(getBASIC()))
