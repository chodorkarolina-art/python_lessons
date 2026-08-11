# lesson38_task4

from lesson38.src.hello import hello


def test_addition():
    assert 2 + 2 == 4


# lesson38_task13
def test_hello():
    assert hello() == "Hello from Python!"
