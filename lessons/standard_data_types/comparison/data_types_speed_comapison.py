def base_formatting():
    name = "John"
    age = 22
    return "Name >>>{} age >>>{}".format(name, age)


def f_formatting():
    name = "John"
    age = 22
    return f"Name >>> {name} age >>> {age}"


def list_comprehension(length):
    return [_ * 2 for _ in range(length)]


def for_loop(length):
    empty_list = []
    for _ in range(length):
        empty_list.append(_ * 2)
    return empty_list


def int_in_list(_int, _list):
    return _int in _list


def int_in_tuple(_int, _tuple):
    return _int in _tuple


def int_in_set(_int, _set):
    return _int in _set


def int_in_dict(_int, _dict):
    return _int in _dict


def timeit_launcher(op_name: str, launch_string: str, repeat_number: int) -> None:
    print(f"{op_name} {timeit.timeit(launch_string, globals=globals(), number=repeat_number)}")


if __name__ == "__main__":
    import timeit
    from dataclasses import dataclass

    N = int(1e5)

    @dataclass
    class Measure:
        name: str
        function: str
        repeat_number: int
        print_sep: bool

    small_sequence = [5, 4, 3, 2, 1]
    sequence = sorted(range(10000), reverse=True)

    small_list = small_sequence
    large_list = sequence

    small_tuple = tuple(small_sequence)
    large_tuple = tuple(sequence)

    small_set = set(small_sequence)
    large_set = set(sequence)

    small_dict = {_: str(_) for _ in small_sequence}
    large_dict = {_: str(_) for _ in sequence}

    for m in (
        Measure("base formatting ", "base_formatting()", N, False),
        Measure("f string ", "f_formatting()", N, True),

        Measure("list comprehension", "list_comprehension(100_000)", 100, False),
        Measure("for loop", "for_loop(100_000)", 100, True),

        Measure("int_in_list", "int_in_list(1, small_list)", N, False),
        Measure("int_in_large_list", "int_in_list(1, large_list)", N, True),

        Measure("int_in_tuple", "int_in_tuple(1, small_tuple)", N, False),
        Measure("int_in_large_tuple", "int_in_tuple(1, large_tuple)", N, True),

        Measure("int_in_set", "int_in_set(1, small_set)", N, False),
        Measure("int_in_large_set", "int_in_set(1, large_set)", N, True),

        Measure("int_in_dict", "int_in_dict(1, small_dict)", N, False),
        Measure("int_in_large_dict", "int_in_dict(1, large_dict)", N, True)
    ):
        timeit_launcher(m.name, m.function, m.repeat_number)
        if m.print_sep:
            print(f"\n{'=' * 100}\n")
