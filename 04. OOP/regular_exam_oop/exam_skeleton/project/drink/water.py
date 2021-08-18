from project.drink.drink import Drink


class Water(Drink):
    COST = 1.50

    def __init__(self, name: str, portion: int, brand: str):
        super().__init__(name, portion, Water.COST, brand)
