from typing import List


class Vet:
    space = 5
    animals = []

    def __init__(self, name: str):
        self.name = name
        self.animals: List = []

    def register_animal(self, animal):
        if Vet.space <= len(Vet.animals):
            return "Not enough space"
        Vet.animals.append(animal)
        self.animals.append(animal)
        return f"{animal} registered in the clinic"

    def unregister_animal(self, animal):
        if animal not in Vet.animals:
            return f"{animal} not in the clinic"
        Vet.animals.remove(animal)
        self.animals.remove(animal)
        return f"{animal} unregistered successfully"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals." \
               f"{Vet.space - len(Vet.animals)} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
