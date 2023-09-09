from typing import Callable
from functools import wraps


def example(func: Callable):
    func.__example = True

    @wraps(func)
    def inner(*args, **kwargs):
        print(f"\n{'=' * 80}\nFunction name >>> {func.__name__}\n{'=' * 80}")
        if func.__doc__:
            print(f"\n{'*' * 80}\nDocstring\n{func.__doc__}\n{'*' * 80}\n")
        result = func(*args, **kwargs)
        print("\n")
        return result
    return inner


def run_examples(some_class: type, *args, **kwargs):
    class_object = some_class(*args, **kwargs)
    attrs = [getattr(class_object, _) for _ in dir(class_object)]
    for attr in attrs:
        try:
            if attr.__example:
                attr()
        except AttributeError:
            pass
