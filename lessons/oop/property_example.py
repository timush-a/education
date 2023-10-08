
class PropertyExample:
    def __init__(self, value: int):
        self.__set_operations_count = 0
        self.__get_operations_count = 0
        self.__del_operations_count = 0
        self.__limited_access_value = value

    def __set(self, value: int):
        self.__set_operations_count += 1
        print(f"Set __limited_access_value {self.__set_operations_count}")
        self.__limited_access_value = value

    def __get(self):
        self.__get_operations_count += 1
        print(f"Get __limited_access_value {self.__get_operations_count}")
        return self.__limited_access_value

    def __del(self):
        self.__del_operations_count += 1
        print(f"Get __limited_access_value {self.__del_operations_count}")
        del self.__limited_access_value

    value = property(__get, __set, __del)


class PropertyDecoratorExample:
    def __init__(self, value: int):
        self.__limited_access_value = value

    @property
    def value(self):
        print("Getter")
        return self.__limited_access_value

    @value.setter
    def value(self, value: int):
        print("Setter")
        self.__limited_access_value = value


if __name__ == "__main__":
    # p = PropertyExample(3)
    # p.value = 4
    # p.value
    # del p.value
    # p.value = 3
    # p.value = 5
    # p.value = 6
    # p.value
    # p.value
    # del p.value

    p_dec = PropertyDecoratorExample(4)
    p_dec.value = 3
    p_dec.value

