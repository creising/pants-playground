from client.utils import add_bang


def test_bang():
    assert add_bang("hello") == "hello!"
