

class DictMethodsExamples:
    def ex_01_create_dict(self) -> None:
        """
        >>> d = {"a": 3, "b": 5}
        >>> d
        {'a': 3, 'b': 5}
        >>> d = {key: value for key, value in zip(["a", "b"], [1, 2])}
        >>> d
        {'a': 1, 'b': 2}
        >>> d = dict(name="John", age=20)
        >>> d
        {'name': 'John', 'age': 20}
        """

    def ex_02_clear(self) -> None:
        """
        >>> d = {"a": 3, "b": 5}
        >>> d.clear()
        >>> d
        {}
        """

    def ex_03_copy(self) -> None:
        """
        >>> d = {"a": 3, "b": 5}
        >>> second_dict = d.copy()
        >>> second_dict
        {'a': 3, 'b': 5}
        """

    def ex_03_get(self) -> None:
        """
        >>> d = {"a": 3, "b": 5}
        >>> d.get("x")
        None
        >>> (d.get("a")
        3
        >>> d.get("x", 0)
        0
        """

    def ex_04_update(self) -> None:
        """
        >>> d = {"a": 3, "b": 5}
        >>> d["a"] = 4
        >>> d
        {'a': 4, 'b': 5}
        >>> d.update(b=7)
        >>> d
        {'a': 4, 'b': 7}
        >>> d.update(c=1)
        >>> d
        {'a': 4, 'b': 7, 'c': 1}
        """

    def ex_05_pop(self) -> None:
        """
        >>> d = {"a": 3, "b": 5}
        >>> d.pop("a")
        3
        >>> d
        {'b': 5}
        """

    def ex_06_popitem(self) -> None:
        """
        >>> d = {'a': 3, 'b': 5}
        >>> d.popitem()
        ('b', 5)
        """

    def ex_07_setdefault(self) -> None:
        """
        >>> d = {'a': 3, 'b': 5}
        >>> d.setdefault('c', 4)
        4
        >>> print(d)
        {'a': 3, 'b': 5, 'c': 4}

        >>> d.setdefault('a', 1)
        3
        >>> d
        {'a': 3, 'b': 5, 'c': 4}
        """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
