from project.food.dessert import Dessert


class Cake(Dessert):
    GRAMS = 250  # (constant)
    CALORIES = 1000  # (constant)
    PRICE = 5  # (constant)

    def __init__(self, name: str, price: float, grams: float, calories: float):
        super().__init__(name, price, grams, calories)
