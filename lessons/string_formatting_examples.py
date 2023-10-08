from typing import Union
from lessons.common.utils import example, run_examples


class StringFormattingExamples:
    @staticmethod
    def square(number: Union[int, float]) -> Union[int, float]:
        return pow(number, 2)

    @example
    def ex_00_string_formatting(self) -> None:
        """
        Форматирование обычной строки без использования позиции
        """
        print("{} {}".format("3.14 square =", self.square(3.14)))

    @example
    def ex_01_string_formatting_with_position(self) -> None:
        """Форматирование обычной строки с использованием позиции"""
        print("{0}, {0}, {1}".format("first", "second"))

    @example
    def ex_02_f_string_formatting(self) -> None:
        """"Форматирование f строки"""
        print(f"Pi square is {self.square(3.14)}")

    @example
    def ex_03_f_string_formatting_float_example(self) -> None:
        """Форматирование f строки с ограничем вывода знаков после запятой"""
        print(f"Pi square is {self.square(3.14):.2f}")

    @example
    def ex_04_f_string_formatting_scientific_notation(self) -> None:
        """Форматирование f строки c использованием экспоненциальная записи"""
        print(f"{int(1e6):.1E} square is {self.square(int(1e6)):.0E}")

    @example
    def ex_05_raw_string_example(self) -> None:
        """Сырые строки"""
        print("raw >>> ", r"a\tb\nc\\d")
        print("regular string >>> ", "a\tb\nc\\d")


if __name__ == "__main__":
    run_examples(StringFormattingExamples)
