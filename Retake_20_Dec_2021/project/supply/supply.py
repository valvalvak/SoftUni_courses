from abc import ABC, abstractmethod


class Supply(ABC):
    @abstractmethod
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        value = value.strip
        if value == "":
            raise ValueError("Name cannot be an empty string.")
        self.name = value

    @property
    def energy(self):
        return self.energy

    @energy.setter
    def energy(self, value):
        if value < 0:
            raise ValueError("Energy cannot be less than zero.")
        self.energy = value
