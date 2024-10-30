import hello


def test_hello(capsys):
    hello.hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"
