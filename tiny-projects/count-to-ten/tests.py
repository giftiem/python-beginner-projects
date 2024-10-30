import count


def test_count(capsys):
    count.count_to_ten()
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"
