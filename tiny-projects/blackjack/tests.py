import blackjack

def test_numbers():
    assert blackjack.value([1, 5, 2, 4]) == 12


def test_named():
    assert blackjack.value([1, 5, "King"]) == 16


def test_ace_11():
    assert blackjack.value([1, "Ace"]) == 12


def test_ace_unequal():
    assert blackjack.value([8, "Ace", "Ace"]) == 20


def test_order():
    assert blackjack.value([8, "King", "Ace"]) == 19
    assert blackjack.value([8, "Ace", "King"]) == 19
    assert blackjack.value(["Ace", 8, "King"]) == 19


def test_naive_ace():
    assert blackjack.value(["King", "Ace", "Ace"]) == 12


def test_natural():
    assert blackjack.value(["Ace", "King"]) == 21


def test_three_aces():
    assert blackjack.value(["Ace", "Ace", "Ace"]) == 13


def test_bust():
    assert blackjack.value([10, 8, "Ace", 5]) == 24


def test_empty():
    assert blackjack.value([]) == 0
