

def fibonacci_of(n: int) -> int:
    """ Calculate fibonacci of a given integer
    Example from: https://realpython.com/fibonacci-sequence-python/

    :param n: int
    :return: int

    >>> fibonacci_of(5)
    5
    >>> fibonacci_of(6)
    8
    >>> fibonacci_of(7)
    13
    >>> fibonacci_of('5')
    Traceback (most recent call last):
        ...
    ValueError: Positive integer number expected, got "5"
    """

    # Validate the value of n
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Positive integer number expected, got "{n}"')

    previous, fib_number = 0, 1
    for _ in range(2, n + 1):
        # Compute the next Fibonacci number, remember the previous one
        previous, fib_number = fib_number, previous + fib_number

    return fib_number


if __name__ == '__main__':
    import doctest
    res = doctest.testmod(verbose=True)
