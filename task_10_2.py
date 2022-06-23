from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculations(self):
        pass


class Coat(Clothes):

    @property
    def calculations(self):
        return round((self.param / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calculations(self):
        return round((self.param * 2) + 0.3)


coat = Coat(20)
suit = Suit(220)
print(coat.calculations)
print(suit.calculations)