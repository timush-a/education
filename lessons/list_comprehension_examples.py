from lessons.common.utils import example, run_examples


class ListComprehensionExamples:
    @example
    def list_comprehension(self) -> None:
        """List comprehension"""
        print([_ for _ in range(10)])

    @example
    def list_comprehension_with_if(self) -> None:
        """List comprehension with filtering"""
        print([number for number in range(10) if number % 2 == 0])

    @example
    def list_comprehension_with_if_else(self) -> None:
        """List comprehension with else condition"""
        print(["odd" if number % 2 == 0 else "even" for number in range(10)])


if __name__ == "__main__":
    run_examples(ListComprehensionExamples)
