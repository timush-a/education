

class TuplesMethodsExamples:
    def ex_01_create_tuple(self) -> None:
        """
        >>> t = tuple(range(1, 4))
        >>> print(t)
        (1, 2, 3)
        >>> t = tuple([1, 2, 3])
        >>> print(t)
        (1, 2, 3)
        >>> t = (1, )
        >>> print(t)
        (1,)
        """

    def ex_02_count(self) -> None:
        """
        >>> t = tuple([1, 1, 1, 2, 3])
        >>> t.count(1)
        3
        """

    def ex_04_index(self) -> None:
        """
        >>> t = tuple([1, 1, 1, 2, 3])
        >>> t.index(3)
        4
        """


if __name__ == "__main__":
    import doctest
    doctest.testmod()


