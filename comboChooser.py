def getBASIC():
   prog = list()
   while True:
      line = input()
      prog.append(line)
      if line.endswith('END') == True:
         return prog # return prog to print(execute(getBASIC()))

def findLine(prog, target):
   for line in prog:
      Line = line.split()
      if (Line[0]) == target:
         return prog.index(line) # return location to execute() line 23

def execute(prog):
  location = 0
  visited = [False] * len(prog)
  while True:
    if location==len(prog)-1: return "success"
    else:
       line = prog[location].split() # now have list of words
       T = line[len(line)-1]
    location = findLine(prog, T) # get new line number
    if visited[location] == True:
       return "infinite loop"
    visited[location] = True

print(execute(getBASIC()))
