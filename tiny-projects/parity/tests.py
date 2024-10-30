import parity


def test_parity():
    assert parity.parity(0) == "even"
    assert parity.parity(5) == "odd"
    assert parity.parity(-1) == "odd"
