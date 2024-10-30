import rps


def test_winner():
    assert rps.winner("rock", "paper") == "p2"
    assert rps.winner("paper", "paper") == "draw"
    assert rps.winner("scissors", "paper") == "p1"