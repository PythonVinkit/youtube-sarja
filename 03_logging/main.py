""" https://docs.python.org/3/howto/logging.html#logging-advanced-tutorial """
import logging.config
import logging
from pathlib import Path

from yaml import load, Loader  # python -m pip install pyyaml
from yaml import Loader


from extra_module import hello_world
from libs import some_module


# logging filters can be used to filter based on _content_, not (only) level
LOGGING_CONFIG = Path("logging.yaml")
# LOGGING_CONFIG = Path("logging_2.yaml")

logging.config.dictConfig(
    config=load(LOGGING_CONFIG.read_text(), Loader=Loader))


logger = logging.getLogger(__name__)


def log_stuff():

    logger.debug("Main funktiossa debug-viesti")
    logger.info("Main funktiossa info-viesti")
    logger.warning("Main funktiossa warning-viesti")
    logger.error("Main funktiossa error-viesti")
    logger.critical("Main funktiossa critical-viesti")

    hello_world()
    some_module.kewl_stuff()

    try:
        1/0
    except Exception:
        logger.error("you did stupid")


if __name__ == '__main__':
    log_stuff()
