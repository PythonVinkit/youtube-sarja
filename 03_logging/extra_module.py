import logging


logger = logging.getLogger(__name__)


def hello_world():
    print("koodin seassa on jossain myös print-käsky")
    logger.debug("extra funktiossa debug-viesti")
    logger.info("extra funktiossa info-viesti")
    logger.warning("extra funktiossa warning-viesti")
    logger.error("extra funktiossa error-viesti")
    logger.critical("extra funktiossa critical-viesti")
