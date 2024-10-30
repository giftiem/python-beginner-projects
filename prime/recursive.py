def is_prime(n, i=2):
    """
    Returns true if number is prime, otherwise returns false
    args:
    n(integer): number to check
    i(integer): current divisor
    returns: 
    boolean
    """
    #Base cases
    if n<=2: 
        return n == 2
    if n%i==0:
        return False
    if i*i>n: # Determine if all possible divisors of n have been checked
        return True
    
    return is_prime(n, i+1)

print(is_prime(13))
print([n for n in range(20) if is_prime(n)])
