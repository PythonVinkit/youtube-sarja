import pytest  # python -m pip install pytest
from .. import fibonacci


def test_correct_values_pytest():
    assert fibonacci.fibonacci_of(5) == 5
    assert fibonacci.fibonacci_of(6) == 8
    assert fibonacci.fibonacci_of(7) == 13


def test_failed_typing_pytest():
    with pytest.raises(ValueError):
        fibonacci.fibonacci_of('5')

