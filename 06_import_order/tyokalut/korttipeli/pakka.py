from abc import abstractmethod
from itertools import product

from .kortti import RanskalainenKortti


class BasePakka:
    _kortti = None

    def __init__(self, kortit):
        self.kortit = kortit

    @abstractmethod
    def uusi_pakka(self):
        raise NotImplementedError("Overwrite this method in real deck")


class Ranskalainen52(BasePakka):
    _kortti = RanskalainenKortti

    @classmethod
    def uusi_pakka(cls):
        kortit = []
        for maa, arvo in product(cls._kortti.ARVOT, cls._kortti.MAAT):
            kortti = cls._kortti(maa=maa, arvo=arvo)
            kortit.append(kortti)
        return cls(kortit)


if __name__ == '__main__':
    pass
    # [print(x) for x in Ranskalainen52.uusi_pakka().kortit]

