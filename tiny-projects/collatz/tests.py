import collatz


def test_collatz_1():
    assert collatz.collatz(1) == 0


def test_collatz_2():
    assert collatz.collatz(2) == 1


def test_collatz_3():
    assert collatz.collatz(3) == 7


def test_collatz_10():
    assert collatz.collatz(10) == 6


def test_collatz_27():
    assert collatz.collatz(27) == 111


def test_collatz_123():
    assert collatz.collatz(123) == 46
