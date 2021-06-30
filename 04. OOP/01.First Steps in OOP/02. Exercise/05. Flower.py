class Flower:
    def __init__(self, name, water_requirements):
        self.name = str(name)
        self.water_requirements = int(water_requirements)

    def water(self, quantity):
        """
        -water(quantity) - it will water the flower.
        Each time check if the quantity is greater than or equal to the required.
        If it is - the flower becomes happy (set is_happy to True).
        """
        pass

    def status(self):
        """
        -status() - it should return "{name} is happy" if the flower is happy,
        otherwise it should return "{name} is not happy".
        """
        pass


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
