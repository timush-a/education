

class StringMethodsExamples:
    def ex_01_capitalize(self) -> None:
        """
        >>> s = "john"
        >>> s.capitalize()
        'John'
        >>> print(s)
        john
        """

    def ex_02_casefold_and_lower(self) -> None:
        """
        >>> s = "JOHN"
        >>> s = s.lower()
        >>> print(s)
        john
        >>> a = chr(926)
        >>> print(a)
        Ξ
        >>> print(chr(913).casefold())
        α
        """

    def ex_03_upper(self) -> None:
        """
        >>> "john".upper()
        'JOHN'
        """

    def ex_04_join(self) -> None:
        """
        >>> "".join([str(_) for _ in list(range(10))])
        '0123456789'
        >>> ", ".join([str(_) for _ in list(range(10))])
        '0, 1, 2, 3, 4, 5, 6, 7, 8, 9'
        """

    def ex_05_zfill(self) -> None:
        """
        >>> "abc".zfill(3)
        'abc'
        >>> "filename.zip".zfill(15)
        '000filename.zip'
        >>> for _ in range(3):
        ...     print(f"{str(_).zfill(5)}.json")
        00000.json
        00001.json
        00002.json
        """

    def ex_06_strip(self) -> None:
        """
        >>> s = "    Hello      world!    "
        >>> s.strip()
        'Hello      world!'

        >>> s = "    Hello world!    "
        >>> s.strip()
        'Hello world!'
        """

    def ex_07_split(self):
        """
        >>> 'a b c d ef'.split()
        ['a', 'b', 'c', 'd', 'ef']
        >>> 'abcdef'.split('d')
        ['abc', 'ef']
        >>> 'abcdef'.split('x')
        ['abcdef']
        """

    def ex_08_replace(self):
        """
        >>> 'aaaabbbbb'.replace('a', 'b')
        'bbbbbbbbb'
        >>> 'aaaabbbbb'.replace('a', 'b', 1)
        'baaabbbbb'
        >>> 'aaaabbbbb'.replace('x', 'b')
        'aaaabbbbb'
        """

    def ex_09_startswith(self):
        """
        >>> 'abcdef'.startswith('a')
        True
        >>> 'abcdef'.startswith('b')
        False
        """

    def ex_10_endswith(self):
        """
        >>> 'config.json'.endswith('.json')
        True
        >>> 'config.json'.endswith('.zip')
        False
        """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
