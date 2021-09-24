import pandas as pd
import matplotlib.pyplot as plt
from helper import parser, min_or_max_of_series

data = pd.read_csv('../data/osakkeet.csv', index_col='PVM', parse_dates=['PVM'], date_parser=parser)

data = data[::-1]
correlations = data.corr()
print(correlations)

maxcorr = correlations.apply(min_or_max_of_series)
mincorr = correlations.apply(min_or_max_of_series, method='min')

minmaxcorr = pd.concat([maxcorr, mincorr]).transpose()
minmaxcorr.columns = ['max', 'max korr', 'min', 'min korr']
print(minmaxcorr)


data.plot(y=['Outokumpu', 'Sanoma'],
          **{'marker': 'o',
             'linewidth': 0.5,
             'markersize': 2,
             'xlabel': 'Päivämäärä',
             'ylabel': 'Keskihinta (€)',
             'figsize': (10, 6)})
plt.show()
