class Cup:
    def __init__(self, size, quantity):
        """
        Create a class called Cup.
        Upon initialization it should receive size(number) and quantity(a number representing how much liquid is in it).
        """
        self.size = int(size)
        self.quantity = int(quantity)

    def fill(self, milliliters):
        """
        fill(milliliters) which will increase the amount of liquid in the cup with the given milliliters
        (if there is space in the cup, otherwise ignore).
        """
        if not milliliters + self.quantity > self.size:
            self.quantity += milliliters

    def status(self):
        """
        :return:
        status() which will return the amount of free space left in the cup.
        """
        return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
