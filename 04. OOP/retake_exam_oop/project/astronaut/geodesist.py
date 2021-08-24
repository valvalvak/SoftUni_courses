from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    breathe_oxygen_units = 10

    def __init__(self, name: str):
        super().__init__(name, 50)
        pass

    def breathe(self):
        self.oxygen -= Geodesist.breathe_oxygen_units
