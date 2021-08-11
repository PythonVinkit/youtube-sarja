import logging
import textwrap


logger = logging.getLogger(__name__)
logger.debug("Import valmis")


def wrap_text(text: str, max_length=40):
    """Rivittää pitkän tekstin kapeampaan muotoon"""
    result = ""
    for paragraph in text.splitlines():
        res = textwrap.wrap(
            paragraph,
            initial_indent="\t",
            subsequent_indent="\t\t ",
            break_long_words=False,
            break_on_hyphens=False,
            width=max_length)
        result += "\n" + "\n".join(res)
    return result
