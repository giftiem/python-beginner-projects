import fibonacci


def test_fibonacci():
    assert fibonacci.fibonacci(0) == 0
    assert fibonacci.fibonacci(1) == 1
    assert fibonacci.fibonacci(2) == 1
    assert fibonacci.fibonacci(3) == 2
    assert fibonacci.fibonacci(4) == 3
    assert fibonacci.fibonacci(5) == 5
    assert fibonacci.fibonacci(6) == 8
