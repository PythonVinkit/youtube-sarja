from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def parser(x):
    return datetime.strptime(x, '%d/%m/%Y')

data = pd.read_csv('../data/osakkeet.csv', index_col='PVM', parse_dates=['PVM'], date_parser=parser)

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
    'figsize': (10,6)})
plt.show()





