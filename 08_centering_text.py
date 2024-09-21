# Waterloo tutorials, 8. Remix, "Centering Text" exercise
# https://cscircles.cemc.uwaterloo.ca/8-remix/

"""For this program, the first line of input is an integer width. Then, 
there are some lines of text; the line "END" indicates the end of the 
text. For each line of text, you need to print out a centered version of 
it, by adding periods .. to the left and right, so that the total length 
of each line of text is width. (All input lines will have length at most 
width.) Centering means that the number of periods added to the left and 
added to the right should be equal if possible; if needed we allow one 
more period on the left than the right. For example, for input
    13
    Text
    in
    the
    middle!
    END
the correct output would be
    .....Text....
    ......in.....
    .....the.....
    ...middle!...
"""

# I redid this and added it here after completing PY101. Not sure what
# solution I came up with the first time through. I tried to solve it
# without using techniques I didn't know about then.


"""Correct outputs for each set of inputs:

.....Text....
......in.....
.....the.....
...middle!...

...........centered...........
.............text.............
..............is..............
.............great............

.........A long, long, time ago.........
........In a galaxy far, far away.......

............There will be 63 characters in this line...........
...............................................................
...............The previous input line was blank...............
.............................--^^--............................

..1.
.un.
.one
eins

"""

inputs = [
    [
        '13',
        'Text',
        'in',
        'the',
        'middle!',
        'END',
    ],
    [
        '30',
        'centered',
        'text',
        'is',
        'great',
        'END',
    ],
    [
        '40',
        'A long, long, time ago',
        'In a galaxy far, far away',
        'END',
    ],
    [
        '63',
        'There will be 63 characters in this line',
        '',
        'The previous input line was blank',
        '--^^--',
        'END',
    ],
    [
        '4',
        '1',
        'un',
        'one',
        'eins',
        'END',
    ],
]

# replaced these first lines with the inputs lists and iterating over them
# width = int(input())
# while True:
#     line = input()
for lines in inputs:
    width = int(lines[0])
    for line in lines[1:len(lines)]:
        # the rest of the solution I used on the website:
        if line == 'END':
            break
        line = '.' * ((width - len(line)) // 2) + line + '.' * ((width - len(line)) // 2)
        if len(line) < width:
            line = '.' + line
        print(line)
    print() # extra line to divide outputs

# Now that I know about the str.center(width) method, it still doesn't
# work here because it adds the extra spacing character on the right
# side, not the left side.