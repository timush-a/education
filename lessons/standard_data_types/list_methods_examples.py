from lessons.common.utils import example, run_examples
import traceback


class ListMethodsExamples:
    @example
    def ex_01_append_to_list(self) -> None:
        """
        a = [1, 2]
        a.append(3)
        print(a) >>> [1, 2, 3]
        """
        a = list((1, 2))
        a.append(3)
        print(a)

    @example
    def ex_02_clear_list(self) -> None:
        """
        a = [1, 2]
        a.clear()
        print(a) >>> []
        """
        a = [1, 2]
        a.clear()
        print(a)

    @example
    def ex_03_copy_list(self) -> None:
        """
        a = [1, 2]
        b = a.copy()
        a.clear()
        print(a) >>> []
        print(b) >>> [1, 2]
        """
        a = [1, 2]
        b = a.copy()
        a.clear()
        print(a)
        print(b)

    @example
    def ex_04_count_value_in_list(self) -> None:
        """
        a = [1, 2, 56]
        print(a.count(1)) >>> 1
        print(a.count(55)) >>> 0
        """
        a = [1, 2, 56]
        print(a.count(1))
        print(a.count(55))

    @example
    def ex_05_clear_list(self) -> None:
        """
        a = [1, 2]
        b = [3, 4]
        print(a.extend(b)) >>> None
        print(a) >>> [1, 2, 3, 4]
        """
        a = [1, 2]
        b = [3, 4]
        print(a.extend(b))
        print(a)

    @example
    def ex_06_index_of_value_in_list(self) -> None:
        """
        a = [1, 2]
        print(a.index(1)) >>> 0
        print(a.index(3)) >>> raise ValueError
        """
        a = [1, 2]
        print(a.index(1))
        try:
            print(a.index(3))
        except Exception as e:
            traceback.print_exception(e)

    @example
    def ex_07_insert_value_in_list(self) -> None:
        """
        a = [1, 2]
        print(a.insert(4, 1)) >>> None
        print(a) >>> [1, 2, 1]

        b = [1, 2, 3]
        print(b.insert(1, "x")) >>> None
        print(b) >>> [1, "x", 2, 3]
        """
        a = [1, 2]
        print(a.insert(4, 1))
        print(a)

        b = [1, 2, 3]
        print(b.insert(1, "x"))
        print(b)

    @example
    def ex_08_pop_value_from_list(self) -> None:
        """
        a = [1, 2, 3, 4, 5]
        print(a.pop()) >>> 5
        print(a.pop(0)) >>> 1
        print(a.pop(-1)) >>> 4
        """
        a = [1, 2, 3, 4, 5]
        print(a.pop())
        print(a.pop(0))
        print(a.pop(-1))

    @example
    def ex_09_remove_value_from_list(self) -> None:
        """
        a = [1, 2, 2, 4, 5]
        print(a.remove(2)) >>> None
        print(a) >>> [1, 2, 4, 5]

        print(a.remove(2)) >>> None
        print(a) >>> [1, 4, 5]

        print(a.remove(2)) >>> raise ValueError
        """
        a = [1, 2, 2, 4, 5]
        print(a.remove(2))
        print(a)

        print(a.remove(2))
        print(a)

        try:
            print(a.remove(2))
        except Exception as e:
            print(e)

    @example
    def ex_10_reverse_list(self) -> None:
        """
        a = [1, 2, 3, 4, 5]
        print(a.reverse())) >>> None
        print(a) >>> [1, 2, 4, 5]
        """
        a = [1, 2, 2, 4, 5]
        print(a.reverse())
        print(a)

    @example
    def ex_11_sort_list(self) -> None:
        """
        a = [3, 2, 5, 4, 1]
        print(a.sort())) >>> None
        print(a) >>> [1, 2, 3, 4, 5]
        """
        a = [3, 2, 5, 4, 1]
        print(a.sort())
        print(a)

    @example
    def ex_12_sort_list_lambda(self) -> None:
        """
        a = [3, 2, 5, 4, 1]
        print(a.sort())) >>> None
        print(a) >>> [1, 2, 3, 4, 5]
        """
        a = ["a", "ab", "aa", "aaab", "aacaa"]
        a.sort()
        print(a)
        a.sort(reverse=True, key=lambda x: len(x))
        print(a)
        a.sort(reverse=False, key=lambda x: len(x))
        print(a)


if __name__ == "__main__":
    run_examples(ListMethodsExamples)
