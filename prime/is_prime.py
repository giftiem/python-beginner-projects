"""
Write a function that returns prime numbers in a list.
Prime sieving is the fastest method.
Prime = div by 1 and itself.
"""

def isPrime(x):
    count = 0
    for denomenator in range(2, x):
        if x%denomenator == 0:
            count += 1
            break
    return (count == 0)


def primes(x):
    primes_list = []
    for n in range(1,x+1):
        if isPrime(n):
            primes_list.append(n)
    return primes_list


def prime_to_index(n):
    primes_list = []
    num = 2
    while len(primes_list) < n:
        if isPrime(num):
            primes_list.append(num)
        num += 1
    return primes_list


def print_prime_triangle(n):
    row_sum = sum(range(n+1))

    prime_list = prime_to_index(row_sum)
    index = 0
    
    for i in range(1,n+1):
        for _ in range(i):
            print(prime_list[index], end = " ")
            index += 1
        print()


# print(primes(80))
print(print_prime_triangle(5))
