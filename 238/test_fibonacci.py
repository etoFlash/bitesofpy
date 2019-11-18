from random import randint
import pytest

from fibonacci import fib


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(5) == 5
    assert fib(9) == 34
    assert fib(15) == 610
    assert fib(22) == 17711
    assert fib(25) == 75025
    for _ in range(10):
        n = randint(0, 30)
        assert fib(n) + fib(n + 1) == fib(n + 2)


def test_value_error():
    with pytest.raises(ValueError):
        assert fib(-1)
    with pytest.raises(ValueError):
        assert fib(-54898)
    with pytest.raises(ValueError):
        assert fib(3.5)


def test_type_error():
    with pytest.raises(TypeError):
        assert fib("z")
    with pytest.raises(TypeError):
        assert fib(None)
    with pytest.raises(TypeError):
        assert fib("")
    with pytest.raises(TypeError):
        assert fib(3, 4)
