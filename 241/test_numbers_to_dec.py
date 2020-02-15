import pytest

from numbers_to_dec import list_to_decimal


def test_list_to_decimal():
    assert list_to_decimal([0, 1, 2, 3]) == 123
    assert list_to_decimal([0, 0]) == 0


def test_error_list_to_decimal():
    with pytest.raises(TypeError):
        list_to_decimal([True])
    with pytest.raises(TypeError):
        list_to_decimal([1, "1"])
    with pytest.raises(ValueError):
        list_to_decimal([0, 5, 11])
    with pytest.raises(ValueError):
        list_to_decimal([9, 10])
