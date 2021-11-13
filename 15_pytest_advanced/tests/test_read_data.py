from pandas import Timestamp

import osake_kuvaaja

EXAMPLE_DATA = (
    "PVM,Nokia\n"
    "30/12/2020,3.168\n"
    "29/12/2020,3.21\n"
    "28/12/2020,3.171"
)


def test_create_file(tmpdir):
    temp_file = tmpdir / "example.csv"
    temp_file.write(EXAMPLE_DATA)

    res = osake_kuvaaja.read_data(str(temp_file))
    assert res.shape == (3, 1)
    assert "Nokia" in res.columns.values
    assert res.index[0] == Timestamp('2020-12-30 00:00:00')

