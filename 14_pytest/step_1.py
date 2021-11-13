from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


# Koodi palasteltu funktioihin
# lisätty funktioihin tyypitykset
# sisääntuleva csv on parametri
# plt.show() -> plt.plot()


def parser(x: str) -> datetime:
    return datetime.strptime(x, '%d/%m/%Y')


def read_data(csv_path: str) -> pd.DataFrame:
    data = pd.read_csv(csv_path, index_col='PVM', parse_dates=['PVM'], date_parser=parser)
    return data


def plot_data(data: pd.DataFrame, do_plots: bool):
    data = data[::-1]
    dataNokia = data[['Nokia']].copy()

    dataNokia['juoksevaKA'] = dataNokia['Nokia'].rolling(window='30D',
                                                         center=True,
                                                         min_periods=5).mean()

    dataNokia.plot(y=['Nokia', 'juoksevaKA'],
                   **{'marker': 'o',
                      'linewidth': 0.5,
                      'markersize': 2,
                      'xlabel': 'Päivämäärä',
                      'ylabel': 'keskihinta (€)',
                      'title': 'Nokia',
                      'figsize': (10, 6)})
    if do_plots:
        plt.show()


def main(do_plots):
    data = read_data('../data/osakkeet.csv')
    plot_data(data, do_plots)


if __name__ == '__main__':
    main(do_plots=True)
