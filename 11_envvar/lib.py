import logging
import urllib.request
from urllib.error import HTTPError

logger = logging.getLogger(__name__)


def get_html_page(url: str, retries: int):
    """ Yksinkertainen esimerkkikoodi, joka noutaa html-sivun.
    :param url: html-sivun osoite
    :param retries: montako kertaa sivu noudetaan virheen sattuessa
    :return: sivun sisältö (binäärinä)
    """
    if not url:
        raise ValueError("Invalid url: %s", url)
    error = None
    for _ in range(retries):
        try:
            logger.debug("Getting url: %s", url)
            page = urllib.request.urlopen(url)
            logger.debug("Response: %s", page.read())
            return page
        except HTTPError as err:
            error = err
    raise error or ConnectionError("Unable to connect to: %s, url")
