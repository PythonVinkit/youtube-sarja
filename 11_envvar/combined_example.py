import argparse
import logging
import os
from types import SimpleNamespace

from lib import get_html_page

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser()

    # URL-parametri, pakollinen arvo
    parser.add_argument(
        '--url',
        dest="url_text",
        required=True,
        help="Anna noudettava url-osoite")

    # Verbose, valinnainen 'flagi', jolla voi aktivoida debug-moodin
    # Vaihtoehto: https://stackoverflow.com/questions/10551117/setting-options-from-environment-variables-when-using-argparse
    parser.add_argument(
        '-v',
        "--verbose",
        action="store_true",
        default=os.getenv("VERBOSE") in ("TRUE", "1"),
        help="Vaihda lokitus DEBUG-moodiin (oletus INFO)")

    # n_retry, valinnainen arvo, jolla oletusarvo. Pakollinen tyyppi int
    parser.add_argument(
        '--n-retry',
        type=int,
        default=3,
        help="Määritä uudelleenyritysten määrä virheen sattuessa (3)"
    )

    args = parser.parse_args()
    logger.info("Käynnistö ohjelma argumentein: %s", args)

    if args.verbose:
        # HUOM! tämä asettaa root-loggerin, ei ainoastaan main-loggerin
        logging.getLogger().setLevel(logging.DEBUG)

    get_html_page(
        url=args.url_text,
        retries=args.n_retry
    )


if __name__ == '__main__':
    main()
