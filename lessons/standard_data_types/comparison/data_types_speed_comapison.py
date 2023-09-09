def base_formatting():
    name = "John"
    age = 22
    return "Name >>>{} age >>>{}".format(name, age)


def f_formatting():
    name = "John"
    age = 22
    return f"Name >>> {name} age >>> {age}"


def list_comprehension():
    return [_ * 2 for _ in range(100)]


def for_loop():
    empty_list = []
    for _ in range(100):
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


if __name__ == "__main__":
    import timeit

    N = int(1e5)

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

    print("base formatting ", timeit.timeit("base_formatting()", globals=globals(), number=N))
    print("f string ", timeit.timeit("f_formatting()", globals=globals(), number=N), "\n")

    print("list comprehension", timeit.timeit("list_comprehension()", globals=globals(), number=N))
    print("for loop", timeit.timeit("for_loop()", globals=globals(), number=N), "\n")

    print("int_in_list", timeit.timeit("int_in_list(1, small_list)", globals=globals(), number=N))
    print("int_in_large_list", timeit.timeit("int_in_list(1, large_list)", globals=globals(), number=N), "\n")

    print("int_in_tuple", timeit.timeit("int_in_tuple(1, small_tuple)", globals=globals(), number=N))
    print("int_in_large_tuple", timeit.timeit("int_in_tuple(1, large_tuple)", globals=globals(), number=N), "\n")

    print("int_in_set", timeit.timeit("int_in_set(1, small_set)", globals=globals(), number=N))
    print("int_in_large_set", timeit.timeit("int_in_set(1, large_set)", globals=globals(), number=N), "\n")

    print("int_in_dict", timeit.timeit("int_in_dict(1, small_dict)", globals=globals(), number=N))
    print("int_in_large_dict", timeit.timeit("int_in_dict(1, large_dict)", globals=globals(), number=N), "\n")
