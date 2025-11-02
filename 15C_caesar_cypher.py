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