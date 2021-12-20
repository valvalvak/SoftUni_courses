from abc import ABC

from project.supply.supply import Supply


class Drink(Supply, ABC):
    def __init__(self, name: str):
        super().__init__(name, 25)
