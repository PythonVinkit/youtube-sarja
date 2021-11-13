import pytest
from pandas import Timestamp
from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt

from unittest.mock import Mock


import osake_kuvaaja

from datetime import datetime


def test_parser():
    # Varmista, että normaalit luvut parsitaan oikein
    assert osake_kuvaaja.parser(x="01/01/2020") == datetime(2020, 1, 1)
    assert osake_kuvaaja.parser(x="31/01/2020") == datetime(2020, 1, 31)

    # Varmista, että virheelliset muodot aiheuttaa virheen
    with pytest.raises(ValueError):
        osake_kuvaaja.parser(x="40/40/2020")
    with pytest.raises(ValueError):
        osake_kuvaaja.parser(x="01-01-2020")


def test_read_data():
    res = osake_kuvaaja.read_data("../data/osakkeet.csv")  # tarkista työhakemisto
    assert res.shape == (2513, 12)
    assert "Nokia" in res.columns.values
    assert res.index[0] == Timestamp('2020-12-30 00:00:00')


def test_main(monkeypatch):
    mocked_read = Mock(return_value="MOCKED")
    mocked_plot = Mock()

    monkeypatch.setattr(osake_kuvaaja, 'read_data',
                        mocked_read, raising=True)

    monkeypatch.setattr(osake_kuvaaja, 'plot_data',
                        mocked_plot, raising=True)

    osake_kuvaaja.main()

    mocked_read.assert_called_once_with('../data/osakkeet.csv')
    mocked_plot.assert_called_once_with("MOCKED")

