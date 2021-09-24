from datetime import datetime
import pandas as pd

date_parser = lambda x: datetime.strptime(x, '%d/%m/%Y')

data = pd.read_csv('osakkeet.csv', index_col='PVM', date_parser=date_parser)
data = data.iloc[::-1]
# print(data.iloc[10:20, 3:6])

print(data.loc[datetime(2011,9,12):datetime(2011,11,3), ['Kemira', 'UPM']])

# print(data.iloc[20:25,3:6])
# print(data.iloc[0,:])
# print(data.iloc[10:20:2, 0:2])





