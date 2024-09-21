# https://cscircles.cemc.uwaterloo.ca/11a-lower-case/

# I redid these and added them here after completing PY101. Not sure what
# solutions I came up with the first time through. I tried to solve them
# without using techniques I didn't know about then.

"""
Step 1: Characters

The first step is to write a function lowerChar(char) that can return 
the result of converting a single character char to lower case. It 
should do the following:

    * if the input character char is a capital letter (between 'A' and 
      'Z'), it should return the lower-case version of the letter 
      (between 'a' and 'z')
    * in all other cases, it should return the same char which was 
      input.

(In order to do the first step, you will have to use an if statement, an 
and operator, and apply some knowledge from the lesson about strings.)
"""

inputs = 'ABZ5 PHmU3p'

def lowerChar(char):
   if ord(char) >= 65 and ord(char) <= 90: # ord('A') == 65; ord('Z') == 90
      return chr(ord(char) + (97 - 65))    # ord('a') == 97
   else:
      return char

for char in inputs:
   print(lowerChar(char))


"""
Step 2: Strings

Now, you will write a second function lowerString(string) which will 
return the result of converting the entire string to lower case, by 
calling lowerChar on each character. We suggest you do this as follows:

    * first, copy the definition of lowerChar(char) from your solution to 
      the first part
    * then define a second function, lowerString(string)
        * on the first line inside lowerString, initialize a variable 
          result = "" equal to the empty string
        * use a for loop with i and set 
          result = result + lowerChar(string[i])
        * finally, return result

Later on, you will learn about the string.lower() method, which is a 
built-in way to perform this task.
"""

inputs = [
   'Gr3aT!',
   'This string has 9 CAPITAL letters (& Punctuation)!',
   'nI)zyqkS07BD!ZH',
]

def lowerChar(char):
   if ord(char) >= 65 and ord(char) <= 90:
      return chr(ord(char) + (97 - 65))
   else:
      return char

def lowerString(string):
   result = ""
   for i in range(len(string)):
      result = result + lowerChar(string[i])
   return result

for string in inputs:
   print(lowerString(string))