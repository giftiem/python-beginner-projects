import primes


def test_primes():
    assert primes.prime(1) == 2
    assert primes.prime(2) == 3
    assert primes.prime(3) == 5
    assert primes.prime(50) == 229
    assert primes.prime(100) == 541