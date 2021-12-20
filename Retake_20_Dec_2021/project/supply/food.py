from abc import ABC

from project.supply.supply import Supply


class Food(Supply, ABC):
    def __init__(self, name: str, energy: int):
        super().__init__(name, 25)
