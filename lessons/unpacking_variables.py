def f1(a: int, b: str, c: dict, *args, d: bool = True, g: int = 4, **kwargs) -> None:
    pass


def f2(*args, value) -> None:
    print(f"{args=}, {value=}")


if __name__ == "__main__":
    f2([1, 2, 3], value=4)
    a, b, c = 1, 2, 3
    print(f"{a=}, {b=}, {c=}")

    d, e, f, *g = 1, 2, 3, 4, 5
    print(f"{d=}, {e=}, {f=}, {g=}")

    *x, y, z, w = 1, 2, 3, 4, 5
    print(f"{x=}, {y=}, {z=}, {w=}")

    x, *y, z = 1, 2, 3, 4, 5, 6, 7
    print(f"{x=}, {y=}, {z=}")

    a = b = c = 777
    print(f"{a == b == c}")
    print(f"{id(a) == id(b) == id(c)=}")


