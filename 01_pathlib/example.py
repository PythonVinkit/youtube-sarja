"""Author: Juhani Takkunen
Tässä tiedostossa olevat koodit liittyvät videoon
(url-tähän kunhan video on julkaistu)

Skriptin ajo saattaa tuhota tiedostoja, eikä ohjelmaa
suunniteltu suoritettavaksi sellaisenaan. Lähdekoodi
on julkaistu ainoastaan, jotta ohjelmasta on mahdollista
kopioida palasia omaan koodiin.
"""

from pathlib import Path
import os

folder_path = Path(r"c:\temp\kansio")

# file_path = os.path.join(folder_path, "my_file.txt")
file_path = folder_path / "my_file.txt"

## Polun osien tarkastelua
# print(file_path.suffix)
# print(file_path.stem)
# print(file_path.parent.parent)

## Polun ominaisuuksien kyselyjä
# print(folder_path.is_file())
# print(folder_path.is_dir())
# print(folder_path.exists())

# Kansion / tiedoston luominen
folder_path.mkdir(exist_ok=True)
# file_path.touch()

# Muunna kaikki tiedostot folder_path -kansiossa second_file.csv nimisiksi
for file in folder_path.iterdir():
    csv_path = file_path.with_suffix(".csv").with_stem("second_file")
    print("Uusi tiedostonimi olisi", csv_path)
    # file.rename(csv_path)  # uudelleennimeää tiedoston

# Tulosta uudet tiedostonimet
for file in folder_path.iterdir():
    print(file)
