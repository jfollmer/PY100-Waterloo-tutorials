# https://cscircles.cemc.uwaterloo.ca/15b-python-pushups/

# I redid this and added it here after completing PY101. I don't know 
# what solution I came up with the first time. I tried to solve it 
# without using techniques I didn't know about then. (I probably didn't
# use these helper functions.)

"""
Coding Exercise: Forty Below In The Winter

In this exercise, you will create a temperature converter which will 
convert Fahrenheit values to Celsius and vice-versa. You will need the 
following two formulas which relate the temperature f in Fahrenheit to 
the temperature c in Celsius:

    f = c * 9/5 + 32
    c = (f - 32) * 5/9

The input will be a string consisting of a floating-point number 
followed immediately by the letter F or C, such as "13.2C". You should 
convert to the other temperature scale and print the converted value in 
the same format. For example, if the input is "8F" then the output 
should be (approximately) "-13.333C", and if the input is "12.5C" then 
the output should be "54.5F".
"""

inputs = ['37.92C', '88.38C', '3.7600000000000002F', '-55.13F', '0C',
          '-40F', '375F']

# input_temp = input() # replaced with inputs list and looping over it

def convert_C_to_F(temp):
   temp = float(temp[:-1])
   return str((temp * (9 / 5)) + 32) + 'F'

def convert_F_to_C(temp):
   temp = float(temp[:-1])
   return str((temp - 32) * (5 / 9)) + 'C'

def convert_temp(temp):
   if temp.endswith('C'):
      return convert_C_to_F(temp)
   elif temp.endswith('F'):
      return convert_F_to_C(temp)

# print(convert_temp(input_temp)) # replaced with the following loop:
for temperature in inputs:
   print(convert_temp(temperature))