from spop.fibonacci import fibonacci


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(17) == 1597
    assert fibonacci(100) == 354224848179261915075
