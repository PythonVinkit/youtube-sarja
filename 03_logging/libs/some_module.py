import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)


def kewl_stuff():
    logger.debug("kewl funktiossa debug-viesti")
    logger.info("kewl funktiossa info-viesti")
    logger.warning("kewl funktiossa warning-viesti")
    logger.error("kewl funktiossa error-viesti")
    logger.critical("kewl funktiossa critical-viesti")