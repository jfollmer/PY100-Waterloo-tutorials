# https://cscircles.cemc.uwaterloo.ca/15c/

# I redid this and added it here after completing PY101. The solution I 
# came up with the first time through is at the very bottom. I tried to 
# solve it without using techniques I didn't know about then.

"""
15C: Caesar's JVTIVK JRCRU IVTZGV

Cryptography is the art and science of hiding the meaning of 
information, in a way that only some people can see it. In this lesson 
we will introduce one of the simplest cryptographic methods, the Caesar 
cipher (http://en.wikipedia.org/wiki/Caesar_cipher) (also known as a 
shift cipher), and you will to write a program to break it. You will 
design every aspect of your solution (unlike lesson 15A, which we broke 
into sub-parts).

The Caesar cipher works by replacing each letter of the alphabet by 
another letter. To be precise, whenever you want to encode some text you 
need to pick a shift value S, which is a number between 0 and 25. Then, 
you replace each letter in the text with the letter which is S positions 
later in the alphabet, circling around to the start after you reach Z at 
the end of the alphabet.

Example:

Suppose we want to encode the secret message

    JOIN ME AT EIGHT BY THE ZOO

using the shift value S=2. The encryption rule says each letter is 
replaced by the one which occurs 2 positions later in the alphabet. For 
example, since the alphabet is ABCDEFGHIJKL..., the first letter J will 
be replaced by the letter L. Continuing, the O is replaced by Q, the I 
is replaced by K, et cetera. To encode the letter Y, we have to circle 
back to the start: after Y comes Z, then A, so Y is replaced by A. 
Likewise Z is replaced by B. So the encoded version of our secret 
message is:

    LQKP OG CV GKIJV DA VJG BQQ

If some spy saw this message, it would not be obvious to them what your 
message was about.

Short Answer Exercise: Spy Coder:
---------------------------------
What is the result of encrypting SPY CODER with the shift value S=5? 
(Use uppercase.) You can write a program in the console to compute this, 
if you like — it might be useful later.
Your answer: 
"""

def caesar_encode(string, shift):
    result = ''
    for char in string:
        if char == ' ':
            result += ' '
        elif ord(char) > ord('Z') - shift:
            result += chr(ord(char) - 26 + shift)
        else:
            result += chr(ord(char) + shift)
    return result

print(caesar_encode('SPY CODER', 5)) # XUD HTIJW

"""
Decoding

Once your friend gets the message, if they know the secret shift value S 
then it is easy for them to decipher the message: each letter is 
replaced by the one appearing S places earlier in the alphabet. For 
example, they would look at L, step back two positions in the alphabet 
and find J, which they now know is the first letter of your secret 
message. Again, they have to treat the alphabet as cyclic, assuming that 
Z comes before A.

Short Answer Exercise: Spy Decoder
----------------------------------
If the encrypted message is HUD, and the shift value is S=6, what was 
the original message? (Use uppercase.)
Your answer:
"""

def caesar_decode(string, shift):
    result = ''
    for char in string:
        if char == ' ':
            result += ' '
        elif ord(char) < ord('A') + shift:
            result += chr(ord(char) + 26 - shift)
        else:
            result += chr(ord(char) - shift)
    return result

print(caesar_decode('HUD', 6)) # BOX

"""
Working for the Bad Guys

You have been hired by a spy to help decipher a message encrypted using 
a shift cipher. Sadly, the spy does not know the value of S. You will 
use statistics to write a program that has a good chance to 
automatically find the right value of S.

Our method will be to use letter frequency analysis. In English, some 
letters are very common (like E) and some are very rare (like J). Here 
is a table of frequencies, based on counting the occurrences in a large 
body of text.

  A       B       C       D       E       F       G       H       I
.0817	.0149	.0278	.0425	.1270	.0223	.0202	.0609	.0697
  J       K       L       M       N       O       P       Q       R
.0015	.0077	.0402	.0241	.0675	.0751	.0193	.0009	.0599
  S       T       U       V       W       X       Y       Z	
.0633	.0906	.0276	.0098	.0236	.0015	.0197	.0007

For example, the frequency of L is .0402=4.02%, which means that in 
average English text, 4.02% of the letters are L.

Call the goodness of a letter its value in the chart above. Then for our 
statistical method, define the goodness of a sentence to equal the sum 
of the goodness of each of its letters. For example the goodness of the 
string GOOD is

    goodness("GOOD") = .0202 + .0751 + .0751 + .0425 = .2129

Now, the idea behind frequency analysis is that strings with higher 
goodness are more likely to represent English text. For example, if the 
spy sees the encoded message "JRRG", this might either represent the 
original text "GOOD" with shift S=3, or "IQQF" with S=1. But the 
goodness of "IQQF" is

    goodness("IQQF") = .0697 + .0009 + .0009 + .0223 = .0938

and since .0938 < .2129, your program should conclude that GOOD is more 
likely to be the correct message than IQQF.

Note: Measuring strings by goodness is not perfect. Say the secret 
message was JAZZ and the secret shift value was S=10, so the encoded 
text was TKJJ. When you input TKJJ to your solver it will try S=10, 
giving JAZZ as a possibility with goodness .0846, but the best is S=5, 
giving OFEE with goodness of .3514 as the program's best guess for the 
secret message. Your program should go ahead and output the non-English 
word OFEE. (Frequency analysis of this type works better if the secret 
message is longer.)

Coding Exercise: Auto-Decryption

Write a program which does the following. First, it should read one line 
of input, which is the encoded message, and will consist of capital 
letters and spaces. Your program must try decoding the message with all 
26 possible values of the shift S; out of these 26 possible original 
messages, print the one which has the highest goodness.

For your convenience, we will pre-define the variable letterGoodness for 
you, a list of length 26 which equals the values in the frequency table 
above,

    letterGoodness = [.0817,.0149,.0278,.0425,.1270,.0223,.0202,...

General advice: ____________________
"""

inputs = [
    (
        'LQKP OG CV GKIJV DA VJG BQQ', 
        'JOIN ME AT EIGHT BY THE ZOO',
    ),
    (
        'UIJT JT B TBNQMF MJOF PG UFYU GPS EFDSZQUJOH',
        'THIS IS A SAMPLE LINE OF TEXT FOR DECRYPTING',
    ),
    (
        'S KW DRO FOBI WYNOV YP K WYNOBX WKTYB QOXOBKV',
        'I AM THE VERY MODEL OF A MODERN MAJOR GENERAL',
    ),
    (
        'DQLMW SQTTML BPM ZILQW ABIZ',
        'VIDEO KILLED THE RADIO STAR',
    ),
    (
        'JAZZ',
        'OFEE',
    ),
    (
        'THE SHIFT COULD ALSO EQUAL ZERO',
        'THE SHIFT COULD ALSO EQUAL ZERO',
    ),
    (
        'CAESARS JVTIVK JRCRU IVTZGV',
        'LJNBJAB SECRET SALAD RECIPE',
    ),
]

letter_goodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 
                   0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 
                   0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 
                   0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 
                   0.0197, 0.0007]

def caesar_decode(string, shift):
    # copied here from above
    result = ''
    for char in string:
        if char == ' ':
            result += ' '
        elif ord(char) < ord('A') + shift:
            result += chr(ord(char) + 26 - shift)
        else:
            result += chr(ord(char) - shift)
    return result

def string_goodness(string):
    goodness = 0
    for char in string:
        if char != ' ':
            alpha_order = ord(char) - ord('A')
            goodness += letter_goodness[alpha_order]
    return goodness

def caesar_brute_decode(encoded):
    max_string = ''
    max_goodness = 0

    for i in range(26):
        decoded = caesar_decode(encoded, i)
        goodness = string_goodness(decoded)
        if goodness > max_goodness:
            max_goodness = goodness
            max_string = decoded

    return max_string

for decoded, encoded in inputs:
    print(caesar_brute_decode(encoded))


"""
Note: The solution above is called a brute force solution since you just 
tried all 26 possibilities. You could have even done this by hand if you 
needed to. Modern cryptographic protocols, on the other hand, are 
designed so that brute force solutions fail, even if you use very fast 
computers to try all possibilities.

If you wanted to make this auto-decoding system more accurate, you could 
pay attention to other English statistics, such as "what letters are 
likely to occur in pairs next to each other? what letters are likely to 
start a word?" This is also useful for more general substitution 
ciphers, where letters replace letters but not in a cyclic way. For such 
ciphers brute force does not work since there are 26*25*...*1 possible 
substitution ciphers, which equals approximately 4 * 1026 (four hundred 
septillion).
"""


# original solution:

string = 'LQKP OG CV GKIJV DA VJG BQQ' # website string #1
         #JOIN ME AT EIGHT BY THE ZOO, i = 24
# string = 'UIJT JT B TBNQMF MJOF PG UFYU GPS EFDSZQUJOH' # website string #2
         #THIS IS A SAMPLE LINE OF TEXT FOR DECRYPTING, i = 25
# string = 'S KW DRO FOBI WYNOV YP K WYNOBX WKTYB QOXOBKV'
# string = 'DQLMW SQTTML BPM ZILQW ABIZ'
# string = 'THE SHIFT COULD ALSO EQUAL ZERO'
# string = 'CAESARS JVTIVK JRCRU IVTZGV'
"""
def encode(string, shiftValue): # returns newString, can be encode or decode really
    newString = str()
    for letter in string:
        newLetter = chr(ord(letter) + shiftValue)
        if letter == ' ': # keep the spaces
            newString = newString + letter
        elif ord(newLetter) > 90: # 90 == 'Z', if positive shiftValue makes it > 'Z', wrap back to 'A'
            newLetter = chr(ord(letter) - 26 + shiftValue)
            newString = newString + newLetter
        elif ord(newLetter) < 65: # 65 == 'A', if negative shiftValue makes it < 'A', wrap back to 'Z'
            newLetter = chr(ord(letter) + 26 + shiftValue)
            newString = newString + newLetter
        else:
            newString = newString + newLetter
    return newString

letterGoodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 
    0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 
    0.0236, 0.0015, 0.0197, 0.0007]
def goodness(newString): # returns stringGoodness
    stringGoodness = float()
    for letter in newString:
        i = ord(letter) - 65 # need i to match index values of letterGoodness
        if i >= 0: # only measure the letters that aren't spaces
            stringGoodness = stringGoodness + letterGoodness[i]
    return stringGoodness

def findGoodness(string):
    potentialGoodness = []
    for shiftValue in range(0, 26): # build potentialGoodness list
        newString = encode(string, shiftValue) # returns newstring
        stringGoodness = goodness(newString) # returns stringGoodness
        potentialGoodness = potentialGoodness + [stringGoodness]
    maxGoodness = max(potentialGoodness)
    bestString = str()
    for shiftValue in range(0, 26): # find the string with maxGoodness
        newString = encode(string, shiftValue) # returns newstring
        stringGoodness = goodness(newString) # returns stringGoodness
        if stringGoodness == maxGoodness:
            bestString = newString
    return bestString
print(findGoodness(string))
"""