import types

from .pakka import BasePakka
from tyokalut.korttipeli import pakka


class RanskalainenKortti:
    ARVOT = range(1, 14)
    MAAT = {"pata", "hertta", "ruutu", "risti"}

    def __init__(self, arvo, maa):
        self.arvo = arvo
        self.maa = maa

    def __str__(self):
        maa = self.maa
        arvo = self.arvo
        return f"RanskalainenKortti({maa=}, {arvo=})"

    def muodosta_pakka(self, deck_object: BasePakka):
    #def muodosta_pakka(self, deck_object):
        return deck_object
