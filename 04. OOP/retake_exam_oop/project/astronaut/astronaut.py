from abc import ABC, abstractmethod


class Astronaut(ABC):
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @abstractmethod
    def breathe(self):
        pass

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
