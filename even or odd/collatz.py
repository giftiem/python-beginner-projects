"""
NOT YET PROVEN
Write a function that will implement the collatz 
conjecture.
The collatz conjecture implements two functions until
the output is one.
The functions are as follows
If the given input(n) is even:
    f(n) = (n)/2
Else if the given input(n) is od:
    f(n) = 3n + 1
"""

def collatz(n):
    sn = [n]
    while n != 1:
        n = n/2 if n % 2 == 0 else (3*n) + 1
        sn.append(int(n))
    return sn

print(collatz(6))
print(collatz(1))

#Can extend this question to see which number in a range gives the 
#longest collatz sequence?


