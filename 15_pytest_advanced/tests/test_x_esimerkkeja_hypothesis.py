from datetime import date
from datetime import datetime
from statistics import mean

from hypothesis import given
from hypothesis.strategies import dates, integers, floats, lists

import osake_kuvaaja
import matikka


@given(dates())
def test_parser(time_val):
    # Varmista, että normaalit luvut parsitaan oikein
    date_str = time_val.strftime('%d/%m/%Y')
    dt = datetime.combine(time_val, datetime.min.time())
    assert osake_kuvaaja.parser(x=date_str) == dt


@given(lists(integers(), min_size=1, max_size=1000))
def test_keskiarvo_integer(items):
    assert abs(matikka.laske_keskiarvo(items) - mean(items)) < 0.000000001


@given(lists(floats(allow_infinity=False,
                    allow_nan=False), min_size=1, max_size=1000))
def test_keskiarvo_float(items):
    assert abs(matikka.laske_keskiarvo(items) - mean(items)) < 0.01

@given(
    lists(
        floats(
            min_value=10e-10,
            max_value=10e10,
            allow_infinity=False,
            allow_nan=False,
        ),
        min_size=1,
        max_size=1000))
def test_keskiarvo_float_2(items):
    assert abs(matikka.laske_keskiarvo(items) - mean(items)) < 0.0001
