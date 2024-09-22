# https://cscircles.cemc.uwaterloo.ca/18-efficiency/

# First time doing this exercise, after finishing PY101.

"""
Don't Compute Unnecessary Things, Even Once

Our second example is about checking whether numbers are prime, which is 
important in cryptography and computer security. A number is prime if it 
has exactly two factors: 1 and itself. The first few prime numbers are 
2, 3, 5, 7, 11, 13, 17, 19, 23. (For example, 21 is not prime because it 
has factors 3 and 7 as well as 1 and 21.)

How can we test whether a number is prime in Python? We saw earlier how 
to test divisibility:

    N % D == 0  # will be True if D is a divisor of N, False otherwise

So by testing all possible divisors, we arrive at the following program.
"""

inputs = [10, 11, 17783, 38771]

def isItPrime(N):
    for D in range(2, N):                   # test D from 2 to N-1
        if N % D == 0:                      # is D a divisor of N?
            print(N, "is not prime; divisible by", D)
            return
    print(N, "is prime")                    # there were no divisors

for num in inputs:
   isItPrime(num)

# outputs:
# 10 is not prime; divisible by 2
# 11 is prime
# 17783 is prime
# 38771 is not prime; divisible by 137

"""
It works! But it is also too slow on large numbers. Pick Enter input and 
type isItPrime(324635459). It runs out of time. Try some more values... 
for primes greater than about 10000000 the code always runs out of time, 
because the grader can only execute the divisibility-checking loop about 
10 million times per second. If we want to check larger numbers, we will 
need a more efficient idea. Let's make the code work even for numbers as 
big as a trillion (1000000000000)!

Do we really need to check all of the numbers between 2 and N-1, to 
check if N is prime?

Hint: No. But why not? Take a few minutes to see if you can come up with 
an idea yourself. Open a copy of the program in the console, and take a
look at how big of a factor the program usually finds, when N is not 
prime.

The idea, and an argument

If you read the hint and experimented, you might have noticed that when 
N is not prime, the program usually found a pretty small factor compared 
to N. For example, isItPrime(34827948723948723984729834) runs pretty 
quickly even though its input is gigantic, finding the divisor D=2.

Maybe we don't actually need to check all possible factors. Is there 
some small limit to the number of factors we need to check, before we 
can be sure that N is prime? Thankfully, yes! In fact we can argue that 
if N is not prime, one of its divisors is at most sqrt(N). Why? Well, if 
N is not prime, then it has a divisor A. Being a divisor means that 
there is some other number B such that

    A * B == N

Let's continue the argument. If A <= sqrt(N) or B <= sqrt(N), then we 
are happy: we found a factor of N that is small, like we wanted. But a
ctually these are the only possibilities: otherwise we get the 
impossible contradiction

    N = A * B > sqrt(N) * sqrt(N) = N

Great! So now, let's implement this new idea in Python. The easiest way 
to change the old approach is to add a test within the for loop: once 
D > sqrt(N) (or equivalently, D * D > N), we can just break out of the 
loop and stop testing:
"""

def isItPrime(N): # same as before
    for D in range(2, N):
        if (D * D > N):          # first added line
            break                  # second added line
        if N % D == 0:
            print(N, "is not prime; divisible by", D)
            return
    print(N, "is prime")

isItPrime(1000006000009)
# 1000006000009 is not prime; divisible by 1000003
isItPrime(1666666009999)
# 1666666009999 is prime

"""
The program now works on gigantic primes!

Final Exercise

In this exercise, we combine the primes from the second half of the 
lesson with the list-based approach of the first half. Your code should 
fill out a table of length 1000001 so that isPrime[N] equals True if N 
is prime, and False if N is composite, for all N up to one million. 
(isPrime[0] and isPrime[1] should be False.)

Big Hint: The solution that we have in mind for this problem is called 
the "Sieve of Eratosthenes." The table is initially filled with `True`;
then you walk through the table starting from index 2 and whenever you 
see a prime number, change all indices corresponding to multiples of 
that prime number to `False`. You should read the wikipedia page for the
full details, and once you understand it, code it up in Python:
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Coding Exercise: Primed for Takeoff

Write a program that defines the table isPrime we described above 
(notice that isPrime is a list, not a function). 

Hint: You don't need to print any output. In fact, printing out a 
million things will make you exceed the time limit. You may want to test
it for an array of length 101 instead of 1000001 first, to make
debugging easier.

The grader will allow a longer-than-usual amount of time, 7 seconds, for 
your program to execute. However, simply using the isItPrime function 
will not be fast enough.
"""

isPrime = [False, False, True] + [True, False] * (999998//2)

for num in range(3, 999999, 2):
   if isPrime[num] == False:
      continue
   for divisor in range(2, num):
      if divisor**2 > num:
         break
      elif num % divisor == 0:
         for i in range(num, 1000001, num):
            isPrime[i] = False
         break
   for i in range(num * 2, 1000001, num):
      isPrime[i] = False
            
# print(isPrime[:1001])
print('done')

# This takes too long for the website (even adding the second function 
# call in their example above takes too long), but my machine does in 
# under 5 seconds.