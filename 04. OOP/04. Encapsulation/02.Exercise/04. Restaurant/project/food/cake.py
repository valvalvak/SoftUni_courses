from project.food.dessert import Dessert


class Cake(Dessert):
    GRAMS = 250  # (constant)
    CALORIES = 1000  # (constant)
    PRICE = 5  # (constant)

    def __init__(self, name: str):
        super().__init__(name, Cake.PRICE, Cake.GRAMS, Cake.CALORIES)
