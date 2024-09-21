# Waterloo tutorials, 8. Remix, "Character Map" exercise
# https://cscircles.cemc.uwaterloo.ca/8-remix/

"""Several lessons ago we showed you the following diagram:

chr:      !   "   #   $   %   &   '   (   )   *   +   ,   -   .   / 
asc: 32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47 
chr:  0   1   2   3   4   5   6   7   8   9   :   ;   <   =   >   ? 
asc: 48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63 
chr:  @   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O 
asc: 64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79 
chr:  P   Q   R   S   T   U   V   W   X   Y   Z   [   \   ]   ^   _ 
asc: 80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95 
chr:  `   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o 
asc: 96  97  98  99  100 101 102 103 104 105 106 107 108 109 110 111
chr:  p   q   r   s   t   u   v   w   x   y   z   {   |   }   ~     
asc: 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 

Write a program which prints out this table. (Character 127 is invisible 
but should be printed out like all the other characters anyway. Extra/
missing space characters at the end of each line don't matter, the 
grader will ignore them.)
"""


# This is the refactored solution I came up with originally, before
# starting the core curriculum.

char = str()
line1 = str()
line2 = str()
for i in range(32, 128):        # the ascii values we want to print
    char = chr(i)               # get character for each ascii value
    if i % 16 == 0:             # word wrap:    each line 16 chars long
        if i >= 48:             #               starting at 47 (end of first set of lines),
            print(line1)        #               print lines before they reset
            print(line2)        #               (these don't print before the first line's done)
        line1 = 'chr:  '        #               give lines labels, and reset lines every 16 chars
        line2 = 'asc: '
    if ord(char) < 100:         # spacing for two digit numbers
        line1 = line1 + char + '   '
        line2 = line2 + str(ord(char)) + '  '
    if ord(char) >= 100:        # adjust spacing for three digit numbers
        line1 = line1 + char + '   '
        line2 = line2 + str(ord(char)) + ' '
print(line1)                    # print final lines since not looping again where the first prints are
print(line2)


"""Below is my first try at a solution, which worked, but it's unwieldy.
What I said at the time:
    I bet I can make this even more concise.
    And I did, see new code up top.
"""

# char = str()

# line1a = 'chr:  '
# line1b = 'asc: '
# for i in range(32, 48):
#     char = chr(i)
#     line1a = line1a + char + '   '
#     line1b = line1b + str(ord(char)) + '  '
# print(line1a)
# print(line1b)

# line2a = 'chr:  '
# line2b = 'asc: '
# for i in range(48, 64):
#     char = chr(i)
#     line2a = line2a + char + '   '
#     line2b = line2b + str(ord(char)) + '  '
# print(line2a)
# print(line2b)

# line3a = 'chr:  '
# line3b = 'asc: '
# for i in range(64, 80):
#     char = chr(i)
#     line3a = line3a + char + '   '
#     line3b = line3b + str(ord(char)) + '  '
# print(line3a)
# print(line3b)

# line4a = 'chr:  '
# line4b = 'asc: '
# for i in range(80, 96):
#     char = chr(i)
#     line4a = line4a + char + '   '
#     line4b = line4b + str(ord(char)) + '  '
# print(line4a)
# print(line4b)

# line5a = 'chr:  '
# line5b = 'asc: '
# for i in range(96, 112):
#     char = chr(i)
#     if ord(char) < 100:
#         line5a = line5a + char + '   '
#         line5b = line5b + str(ord(char)) + '  '
#     if ord(char) >= 100:
#         line5a = line5a + char + '   '
#         line5b = line5b + str(ord(char)) + ' '
# print(line5a)
# print(line5b)

# line6a = 'chr:  '
# line6b = 'asc: '
# for i in range(112, 128):
#     char = chr(i)
#     line6a = line6a + char + '   '
#     line6b = line6b + str(ord(char)) + ' '
# print(line6a)
# print(line6b)