def explanation(exp_str: str):
    def outer(func):
        def inner(*args, **kwargs):
            print(f"{'=' * 80}\n{exp_str}\n{'=' * 80}")
            result = func(*args, **kwargs)
            print()
            return result
        return inner
    return outer


def example(func):
    func.__example__ = True
    return func


def run_examples(some_class: type, *args, **kwargs):
    class_object = some_class(*args, **kwargs)
    attrs = [getattr(class_object, _) for _ in dir(class_object)]
    for attr in attrs:
        try:
            if attr.__example__:
                attr()
        except AttributeError:
            pass
