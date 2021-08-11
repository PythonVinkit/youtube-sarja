from tyokalut.korttipeli import pakka


def main():

    korttipakka = pakka.Ranskalainen52.uusi_pakka()
    for x in korttipakka.kortit:
        print(x)


if __name__ == '__main__':
    main()
