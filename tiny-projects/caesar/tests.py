import caesar


def test_pangram_13():
    pangram = "the quick brown fox jumps over the lazy dog"
    shifted = "gur dhvpx oebja sbk whzcf bire gur ynml qbt"

    assert caesar.shift(13, pangram) == shifted
    assert caesar.shift(13, shifted) == pangram


def test_hello():
    n = 3
    text = "hello"
    assert caesar.shift(n, text) == "khoor"


def test_world():
    n = 1
    text = "world"
    assert caesar.shift(n, text) == "xpsme"


def test_shift_26():
    n = 26
    text = "abcxyz"
    assert caesar.shift(n, text) == "abcxyz"


def test_shift_0():
    n = 0
    text = "wethinkcode"
    assert caesar.shift(n, text) == "wethinkcode"


def test_shift_negative():
    n = -2
    text = "python"
    assert caesar.shift(n, text) == "nwrfml"


def test_empty():
    n = 5
    text = ""
    assert caesar.shift(n, text) == ""


def test_punctuation():
    n = 2
    text = "hello, world!"
    assert caesar.shift(n, text) == "jgnnq, yqtnf!"