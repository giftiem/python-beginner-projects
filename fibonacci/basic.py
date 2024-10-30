def fib_sequence(n):
    """
    Write a function to store the fibonacci sequence upto
    the nth element in a list.
    """
    terms = [0] * n
    terms[0] = 1
    terms[1] = 1

    for k in range(0, n-1, 1):
        terms[k+1] = terms[k] + terms[k-1]

    return terms


print(fib_sequence(100))