from typing import Union
from lessons.common.utils import explanation, example, run_examples


class StringExamples:
    def __init__(self):
        pass

    @staticmethod
    def square(number: Union[int, float]) -> Union[int, float]:
        return pow(number, 2)

    @example
    @explanation("Форматирование обычной строки без использования позиции")
    def string_formatting(self) -> None:
        print("{}, {}".format("3.14 square =", self.square(3.14)))

    @example
    @explanation("Форматирование обычной строки с использованием позиции")
    def string_formatting_with_position(self) -> None:
        print("{1}, {0}, {2}".format("zero", "first", "second"))

    @example
    @explanation("Форматирование f строки")
    def f_string_formatting(self) -> None:
        print(f"Pi square is {self.square(3.14)}")

    @example
    @explanation("Форматирование f строки с ограничем вывода знаков после запятой")
    def f_string_formatting_float_example(self) -> None:
        print(f"Pi square is {self.square(3.14):.2f}")

    @example
    @explanation("Форматирование f строки c использованием экспоненциальная записи")
    def f_string_formatting_scientific_notation(self) -> None:
        print(f"{int(1e6)} square is {self.square(int(1e6)):.0E}")

    @example
    @explanation("Сырые строки")
    def raw_string_example(self) -> None:
        print("raw >>> ", r"a\tb\nc\\d")
        print("regular string >>> ", "a\tb\nc\\d")


if __name__ == "__main__":
    run_examples(StringExamples)
