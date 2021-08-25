import argparse
import logging

from lib import get_html_page

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_arguments():
    parser = argparse.ArgumentParser()

    # URL-parametri, pakollinen arvo
    parser.add_argument(
        '--url',
        dest="url_text",
        required=True,
        help="Anna noudettava url-osoite")

    # Verbose, valinnainen 'flagi', jolla voi aktivoida debug-moodin
    parser.add_argument(
        '-v',
        "--verbose",
        action='store_true',
        help="Vaihda lokitus DEBUG-moodiin (oletus INFO)")

    # n_retry, valinnainen arvo, jolla oletusarvo. Pakollinen tyyppi int
    parser.add_argument(
        '--n-retry',
        type=int,
        default=3,
        help="Määritä uudelleenyritysten määrä virheen sattuessa (3)"
    )

    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    logger.info("Käynnistä ohjelma argumentein: %s", args)

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    res = get_html_page(
        url=args.url_text,
        retries=args.n_retry
    )
    logger.info("Res: %s", res)

    # Lisää mahdollisuuksia:
    # - monimutkaisempia (tyyppi) validointeja, esim. päivämäärä
    # - useita parametrejä (lista)
    # - parsereita voi yhdistellä, ns. sub_parser


if __name__ == '__main__':
    main()
    # python .\argparse_example.py --url https://gist.githubusercontent.com/prabansal/115387/raw/0e5911c791c03f2ffb9708d98cac70dd2c1bf0ba/HelloWorld.txt --n-retry 3
