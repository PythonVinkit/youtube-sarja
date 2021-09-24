from datetime import datetime
import pandas as pd

def parser(date: str):
    """ Parses dates in formt D/M/YYYY to datetime

    Args:
        date (str): date string

    Returns:
        datetime: date string as datetime object
    """
    return datetime.strptime(date, '%d/%m/%Y')


def min_or_max_of_series(col: pd.Series, method='max'):
    """Calculates max or min index and value of a pandas series

    Args:
        col (pd.series): [description]
        method (str, optional): 'min' for calculating minimum, 'max' for maximum. Defaults to 'max'.

    Returns:
        tuple: First element is the index and second value of the operation
    """
    if method == 'max':
        col = col.drop(labels=[col.name])
        return (col.idxmax(), col.max())
    elif method == 'min':
        return (col.idxmin(), col.min())
