

class Animal:
    legs: int

    def __init__(self, legs: int = 4):
        self.legs = legs

    def run(self):
        if self.legs >= 0:
            print('Lies')
        if self.legs == 1:
            print('Jump')
        if self.legs >= 1:
            print('Run')


class Chicken(Animal):
    ...


class Dog(Animal):
    def __init__(self):
        super().__init__()

    @classmethod
    def tail(cls):
        print(True)

    def bark(self):
        print(f"{self.__class__} Wof")


class Cat(Animal):
    def bark(self):
        print(f"{self.__class__} can't bark")


class CatDog(Cat, Dog):
    @classmethod
    def tail(cls):
        print(False)


class UnknowAnimal(Chicken, CatDog):
    ...


if __name__ == "__main__":
    Dog.tail()
    dog = Dog()
    dog.bark()

    cat = Cat()
    cat.bark()

    cat_dog = CatDog()
    cat_dog.bark()
    cat_dog.tail()

    unknown = UnknowAnimal()
    unknown.bark()

    print(*[c.__name__ for c in UnknowAnimal.mro()], sep=' >>> ')
