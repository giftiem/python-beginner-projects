import factors


def test_factors():
    assert factors.factors(26) == {2, 13}
    assert factors.factors(60) == {2, 3, 5}
    assert factors.factors(1) == set()