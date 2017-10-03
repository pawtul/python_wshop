def suma(a, b):
    """
    >>> suma(1, 3)
    4

    >>> suma(44, 56)
    100

    >>> suma('a', 44)
    Traceback (most recent call last):
     ...
    TypeError: cannot concatenate 'str' and 'int' objects

    """
    return a + b


if __name__ == '__main__':
    import doctest
    doctest.testmod()
