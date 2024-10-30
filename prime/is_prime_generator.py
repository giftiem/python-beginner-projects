"""
Write a function that checks if numbers in a specific
range are prime using generators
"""

def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True

    for k in range(2,x):
        return x%k != 0

def primeGenerator(x,y):
    for x in range(x,y):
        if isPrime(x):
            yield(x)