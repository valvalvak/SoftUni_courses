class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self.topping_type

    @topping_type.setter
    def topping_type(self, value):
        if len(value) < 1:
            raise ValueError("The topping type cannot be an empty string")
        self.topping_type = value

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, value):
        if value < 1:
            raise ValueError("The weight cannot be less or equal to zero")
        self.weight = value
