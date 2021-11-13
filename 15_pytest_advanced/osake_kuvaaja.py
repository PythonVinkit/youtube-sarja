from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


# Koodi palasteltu funktioihin
# lisätty funktioihin tyypitykset
# sisääntuleva csv on parametri
# plt.show() -> plt.plot()


def parser(x: str):
    return datetime.strptime(x, '%d/%m/%Y')


def read_data(csv_path: str) -> pd.DataFrame:
    data = pd.read_csv(
        csv_path,
        index_col='PVM',
        parse_dates=['PVM'],
        date_parser=parser)
    return data


def plot_data(data: pd.DataFrame):
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
    plt.plot()
    return plt


def main():
    data = read_data('../data/osakkeet.csv')
    plot = plot_data(data)
    plot.show()


if __name__ == '__main__':
    main()
