from sort import swap, sort

# Tests for swap()

def test_swap_middle():
    numbers = [1, 2, 3, 4, 5]
    swap(numbers, 2, 3)
    assert numbers == [1, 2, 4, 3, 5]


def test_swap_ends():
    numbers = [1, 2, 3, 4, 5]
    swap(numbers, 0, 4)
    assert numbers == [5, 2, 3, 4, 1]


def test_swap_same():
    numbers = [1, 2, 3, 4, 5]
    swap(numbers, 1, 1)
    assert numbers == [1, 2, 3, 4, 5]


def test_swap_negative():
    numbers = [-1, 0, 1]
    swap(numbers, 0, -1)
    assert numbers == [1, 0, -1]


def test_swap_single():
    numbers = [42]
    swap(numbers, 0, 0)
    assert numbers == [42]

# Tests for sort()

def test_sort_basic():
    numbers = [4, 2, 7, 1, 5]
    sort(numbers)
    assert numbers == [1, 2, 4, 5, 7]


def test_sort_sorted():
    numbers = [1, 2, 4, 5, 7]
    sort(numbers)
    assert numbers == [1, 2, 4, 5, 7]


def test_sort_negative():
    numbers = [9, 6, 3, 0, -2]
    sort(numbers)
    assert numbers == [-2, 0, 3, 6, 9]


def test_sort_repeated():
    numbers = [5, 2, 9, 2, 5]
    sort(numbers)
    assert numbers == [2, 2, 5, 5, 9]


def test_sort_empty():
    numbers = []
    sort(numbers)
    assert numbers == []


def test_sort_single():
    numbers = [3]
    sort(numbers)
    assert numbers == [3]


def test_sort_large():
    numbers = [7, 3, 9, 2, 1, 5, 8, 4, 6, 0]
    sort(numbers)
    assert numbers == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
