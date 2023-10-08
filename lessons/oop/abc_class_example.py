from abc import ABC, abstractmethod


class Car(ABC):
    wheels = 4

    def __init__(self, color: str = 'white', model=None):
        self.color = color
        self.model = model

    @abstractmethod
    def drive(self): ...


class Dodge(Car):
    def __init__(self, color: str, model: str):
        super().__init__(color, model)

    def drive(self):
        print(f"{self.model} {self.color} is driving")


if __name__ == "__main__":
    challenger = Dodge('black', 'cf3')
    challenger.drive()
