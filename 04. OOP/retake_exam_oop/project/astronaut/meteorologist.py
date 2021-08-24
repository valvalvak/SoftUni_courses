from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    breathe_oxygen_units = 15

    def __init__(self, name: str):
        super().__init__(name, 90)
        pass

    def breathe(self):
        self.oxygen -= Meteorologist.breathe_oxygen_units
