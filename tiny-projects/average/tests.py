from average import average


def test_average_positive():
    numbers = [1, 2, 3, 4, 5]
    assert average(numbers) == 3.0


def test_average_negative():
    numbers = [-1, -2, -3, -4, -5]
    assert average(numbers) == -3.0


def test_average_mixed():
    numbers = [2, -4, 6, -8, 10]
    assert average(numbers) == 1.2


def test_average_half():
    numbers = [0.5, 1.5, 2.5, 3.5, 4.5]
    assert average(numbers) == 2.5


def test_average_single():
    numbers = [7]
    assert average(numbers) == 7.0