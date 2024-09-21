# https://cscircles.cemc.uwaterloo.ca/15b-python-pushups/

# I redid this and added it here after completing PY101. I don't know 
# what solution I came up with the first time. I tried to solve it 
# without using techniques I didn't know about then. (I probably didn't
# use these helper functions.)

"""
Coding Exercise: Poetic Analysis

A writer is working on their newest poem, Turing and the Machines. 
They have hired you to determine the word which appears the most times. 
You can access the lines of the poem by calling input() repeatedly, and 
the last line contains the three characters ###. All lines consist of 
words separated by single spaces; there are no digits or punctuation. 
Convert all the words to lower-case, and print the word that occurs the 
most times (we guarantee there will not be a tie). For example, if the 
input is

    Here is a line like sparkling wine
    Line up fast or be the last
    ###

Then the output should be

    line

since it appears twice and no other word appears twice.
"""

inputs = [
    [
        'Here is a line like sparkling wine',
        'Line up now behind the cow',
        '###',
    ],
    [
        'The word the appears twice',
        '###',
    ],
    [
        'There once was some code from Atlanta',
        'Created by elves who drank Fanta',
        'It always would show',
        'Ho ho ho ho ho',
        'Since twas a lil helper for Santa',
        '###',
    ],
    [
        'Turing made a simple test',
        'To check if computers were the best',
        'Could a computer write a poem better than this',
        'It might be a hit but it might be a miss',
        '###',
    ],
    [
        'soliloquy',
        '###',
    ],
]

def get_lines(lines):
    # replaced this loop...:
    # lines = []
    # while True:
    #     line = input()
    #     lines.append(line.lower())
    #     if line == '###':
    #         break

    # ...with this one, and the `lines` argument in this function:
    for i in range(len(lines)):
        lines[i] = lines[i].lower()
    return lines

def convert_lines_to_words(poem):
    words = []
    for line in poem:
        words += line.split()
    return words

def count_words(words):
    word_counts = []
    for word in words:
        word_counts.append(words.count(word))
    return word_counts

def most_frequent_word(poem):
    poem = get_lines(poem) # added the `poem` parameters to the
                           # `most_frequen_word(poem)` and 
                           # `get_lines(poem)` functions
    words = convert_lines_to_words(poem)
    word_counts = count_words(words)

    for i in range(len(word_counts)):
        if word_counts[i] == max(word_counts):
            return words[i]

# print(most_frequent_word()) # replaced with the following loop:
for poem in inputs:
    print(most_frequent_word(poem))