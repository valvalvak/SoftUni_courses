from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50  # (constant)
    PRICE = 3.50  # (constant)

    def __init__(self, name: str, price: float, milliliters: float, caffeine: float):
        super().__init__(name, price, milliliters)
        self.caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, value):
        self.__caffeine = value
