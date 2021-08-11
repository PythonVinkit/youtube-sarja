# --- Standard library ---
import logging

# --- Third party ---
# import requests
# import pandas

# --- Local packages ---
# Loggerin voisi alustaa ennen seuraavia importteja, jos haluaa seurata
# importin yhteydessä tapahtuvia lokituksia.
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Valid:
from tyokalut.tekstin_muokkaus import wrap_text
from tyokalut import tekstin_muokkaus  # muuttuja = tekstin_muokkaus
import tyokalut.tekstin_muokkaus  # muuttuja = tyokalut

# Invalid
# import tyokalut
# from tyokalut.tekstin_muokkaus import *  # still invalid, if it works

logger.info("tyokalut nimi: %s", tyokalut.__name__)
logger.info("tyokalut __file__: %s", tyokalut.__file__)
logger.info("tyokalut PUPPUTEKSTI: %s", tyokalut.PUPPUTEKSTI)
logger.info("Pääohjelman importit valmiit")


def main():

    lainaus = """The Module Search Path
    https://docs.python.org/3/tutorial/modules.html#the-module-search-path
    
    When a module named spam is imported, the interpreter first searches for a built-in module with that name. If not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path. sys.path is initialized from these locations:
    
    - The directory containing the input script (or the current directory when no file is specified).
    - PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
    - The installation-dependent default.
    
    Also: https://youtu.be/0oTh1CXRaQ0
    """

    logger.info(wrap_text(lainaus))

    logger.info(tekstin_muokkaus.wrap_text(lainaus))

    logger.info(tyokalut.tekstin_muokkaus.wrap_text(lainaus))


if __name__ == '__main__':
    main()
