from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    breathe_oxygen_units = 5

    def __init__(self, name: str):
        super().__init__(name, 70)
        pass

    def breathe(self):
        self.oxygen -= Biologist.breathe_oxygen_units
