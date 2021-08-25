import logging
import os
from types import SimpleNamespace

from lib import get_html_page

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    args = SimpleNamespace(
        url_text=os.getenv("URL"),
        verbose=os.getenv("VERBOSE") in ("TRUE", "1"),
        n_retry=os.getenv("N_RETRY", 3),
    )

    logger.info("Käynnistö ohjelma argumentein: %s", args)

    if args.verbose:
        logger.setLevel(level=logging.DEBUG)

    get_html_page(
        url=args.url_text,
        retries=args.n_retry
    )


if __name__ == '__main__':
    main()
