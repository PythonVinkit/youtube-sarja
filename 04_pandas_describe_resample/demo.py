import pandas as pd

data20 = pd.read_csv('../data/kumpula_heinakuu_2020.csv',
                     parse_dates={"PVM": ["Vuosi", "Kk", 'Pv', 'Klo']}, index_col='PVM')
data21 = pd.read_csv('../data/kumpula_heinakuu_2021.csv',
                     parse_dates={"PVM": ["Vuosi", "Kk", 'Pv', 'Klo']}, index_col='PVM')

# Aluksi data 20 indeksit eivät ole muuttuneet datetimeksi
print(data21.head())
print(data21.index.dtype)
print(data20.head())
print(data20.index.dtype)

# Muutetaan data20 indeksi datetimeksi
data20.index = pd.to_datetime(data20.index, format='%Y %m %d %H.%M')
print(data20.head(20))
print(data20.index.dtype)

# Katsotaan millainen on pandas.DataFrame.describe()
print(data20.describe())

print(data21.describe())

# Muutetaan sademäärä kuukausittaiseksi arvoksi summaamalla 10 min havaintojen yli
sade_20 = data20.loc[:, ['Sademäärä (mm)']].resample('D').sum()
sade_21 = data21.loc[:, ['Sademäärä (mm)']].resample('D').sum()

# katsotaan describe uudelleen
print(sade_20.describe())
print(sade_21.describe())
