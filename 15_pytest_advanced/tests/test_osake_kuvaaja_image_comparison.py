from matplotlib.testing.decorators import image_comparison

import osake_kuvaaja


@image_comparison(baseline_images=['osakkeet'], remove_text=True,
                  extensions=['png'])
def test_plot_data():
    data = osake_kuvaaja.read_data("../data/osakkeet.csv")
    osake_kuvaaja.plot_data(data)

