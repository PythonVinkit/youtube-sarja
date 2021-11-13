import pytest
from pandas import Timestamp
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
from contextlib import nullcontext as does_not_raise

from unittest.mock import Mock


import osake_kuvaaja

from datetime import datetime


@pytest.mark.parametrize(
    "date_val,result",
    [
        ("01/01/2020", datetime(2020, 1, 1)),
        ("31/01/2020", datetime(2020, 1, 31)),
    ]
)
def test_parser_1(date_val, result):
    assert osake_kuvaaja.parser(x=date_val) == result

@pytest.mark.parametrize(
    "date_val",
    [
        ("40/40/2020"),
        ("01-01-2020"),

    ]
)
def test_parser_2(date_val):
    with pytest.raises(ValueError):
        osake_kuvaaja.parser(x=date_val)


@pytest.mark.parametrize(
    "date_val,expectation,result",
    [
        ("01/01/2020", does_not_raise(), datetime(2020, 1, 1)),
        ("31/01/2020", does_not_raise(), datetime(2020, 1, 31)),
        ("40/40/2020", pytest.raises(ValueError), None),
        ("01-01-2020", pytest.raises(ValueError), None),

    ]
)
def test_parser_3(date_val, expectation, result):
    with expectation:
        assert osake_kuvaaja.parser(x=date_val) == result

