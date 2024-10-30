import count


def test_count(capsys):
    count.count_from_ten()
    captured = capsys.readouterr()
    assert captured.out == "10\n9\n8\n7\n6\n5\n4\n3\n2\n1\n"
