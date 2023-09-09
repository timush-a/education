from pympler.asizeof import asizeof
import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class SlotsPoint:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y


def func(x, y):
    return y, x


if __name__ == "__main__":
    print(f"None {asizeof(None)=}\n")
    print(f"Ellipsis {asizeof(...)=}\n")

    print(f"str {asizeof('a')=}\n")
    print(f"str {sys.getsizeof('a')=}\n")

    print(f"int {asizeof(1)=}")
    print(f"int {asizeof(int(1e20))=}\n")

    print(f"float {asizeof(1/3)=}\n")

    print(f"empty dict {asizeof(dict())=}")
    print(f"dict {asizeof({'a': [1, 2, 3, 4, 5]})=}\n")

    print(f"empty list {asizeof(list())=}")
    print(f"list {asizeof([1, 2, 3, 4, 5])=}\n")

    print(f"empty tuple {asizeof(tuple())=}")
    print(f"tuple {asizeof(tuple([1, 2, 3, 4, 5]))=}\n")

    print(f"empty set {asizeof(set())=}")
    print(f"set {asizeof({1, 2, 3, 4, 5})=}\n")

    print(f"function {asizeof(func(1, 1))=}\n\n")

    print(f"class {asizeof(Point(1, 1))=}\n")
    print(f"class {asizeof(SlotsPoint(1, 1))=}\n")
