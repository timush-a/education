from dataclasses import dataclass


@dataclass
class Data:
    length: int
    values: list
    default_values = [1, 2, 3]

    def get_values_sum(self):
        return sum(self.values)

    def get_default_values(self):
        return self.default_values

    def __str__(self):
        return f"Custom str method {self.values, self.length, self.default_values}"

    def __add__(self, other):
        return self.length + other.length


if __name__ == "__main__":
    data_example = Data(1, [4, 5, 6])
    print(f"{data_example.get_values_sum()=}")
    print(f"{data_example.get_default_values()=}")
    print(data_example + Data(2, [4, 5, 6]))
    print(data_example.values)

    data_example_kw = Data(length=1, values=[3, 4, 5])
    data_example_kw.default_values.append(1)
    print(data_example_kw)

    # data_example_kw = Data(length=1, values=[3, 4, 5], default_values=[0])
