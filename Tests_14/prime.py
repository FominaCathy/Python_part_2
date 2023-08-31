def is_prime(p: int) -> bool:
    """
    Checks the number P for simplicity using finding the
    remainder of the division in the range [2, P).
    >>> is_prime(42)
    False
    >>> is_prime(7)
    True
    >>> is_prime(100000007)
    If the number P is prime, the check may take a long time. Working...
    True
    """

    if p > 100000000:
        print('If the number P is prime, the check may take a long time. Working...')
    for i in range(2, p):
        if p % i == 0:
            return False
    return True


if __name__ == "__main__":
    # help(is_prime)
    import doctest

    # doctest.testmod(verbose=True)
    doctest.testfile('prime.md', verbose=True)
