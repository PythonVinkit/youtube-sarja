from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('../data/osakkeet.csv')
# Kokeile myös index_col = 'PVM'
print(data.head())

# Aluksi päivät ovat vain stringejä!
data['PVM'] = pd.to_datetime(data['PVM'], infer_datetime_format=True)
# # TAI data['PVM'] = pd.to_datetime(data['PVM'], format='%d/%m/%Y')
# # TAI parse_dates=['PVM']
print(data['PVM'])
print(data['PVM'].dtype)

# Sarakkeen valitseminen
dataNokia = data[['PVM', 'Nokia']]
# print(dataNokia.head())

# Sarakkeen lissääminen

dataNokia['juoksevaKA'] = dataNokia['Nokia'].rolling(window=30).mean().fillna(method='ffill')

print(dataNokia.head())

#Sarakkeen lisääminen

#Rivin valitseminen
# print(dataNokia[10:20:2])
print(dataNokia[data['PVM'] > datetime(2020,4,29)])

#Flip 
dataNokia = dataNokia[::-1].reset_index(drop=True)

print(dataNokia.head())

maski1 = dataNokia['PVM'] > '20110501'
maski2 = dataNokia['PVM'] < '20110529'

print(maski1)
print(maski2)

print(maski1 & maski2)
print(dataNokia[maski1 & maski2])

# print(dataNokia[((dataNokia['PVM'] > datetime(2011,5,1)) & (dataNokia['PVM'] < datetime(2011,5,29)))])

# Plot
ax = dataNokia.plot(x='PVM', y=['Nokia', 'juoksevaKA'], linewidth=3, fontsize=18, title='Nokia')
ax.set_xlabel('PVM',fontsize=18)
ax.set_ylabel('Hinta (€)', fontsize=18)
ax.properties()['children'][0].set_linestyle('None')
ax.properties()['children'][0].set_marker('o')
ax.properties()['children'][0].set_markersize(5)
ax.properties()['children'][0].set_markeredgecolor('gray')
ax.properties()['children'][1].set_color('k')

ax.legend(fontsize=14)
plt.show()
