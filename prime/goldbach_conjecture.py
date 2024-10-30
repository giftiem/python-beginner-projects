"""
DISPROVEN
Write a function that returns the smallest odd composite that
does not follow the following 'other' conjecture.
The goldbach conjecture, aka the twin-prime conjecture
proposed by Christian goldbach in the year 1742 states
that every even natural number greater than two is the 
sum of two prime numbers.
His other conjecture states that every odd composite number
can be written as the sum of a prime and twice a square.
"""
import is_prime

def other_conjecture(n):
    primes_list = is_prime.primes(n)
    for k in primes_list:
        conjecture = (n - k)/2
        return conjecture == (conjecture**(1/2))**2
    

num = 1

#simplified using De Morgan Identities
while is_prime.isPrime(num) or other_conjecture(num):
    num += 2

print(f"The number {num-2} cannot be expressed as [prime + 2*(num**2)].")
