from typing import List


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, worker_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__worker_capacity = worker_capacity
        self.animals: List = []
        self.workers: List = []

    def add_animal(self, animal, price):
        if self.__budget < animal.money_for_care + price:
            return "Not enough budget"
        elif len(self.animals) + 1 > self.__animal_capacity:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= animal.money_for_care + price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        pass

    def fire_worker(self, worker_name):
        pass

    def pay_workers(self):
        pass

    def tend_animals(self):
        pass

    def profit(self, amount):
        pass

    def animals_status(self):
        """
        :return:
        You have {total_animals_count} animals
        ----- {amount_of_lions} Lions:
        {lion1}
        ...
        ----- {amount_of_tigers} Tigers:
        {tiger1}
        ...
        ----- {amount_of_cheetahs} Cheetahs:
        {cheetah1}
        ...
        Hint: use the __repr__ methods of the animals to print them on the console
        """
        pass

    def workers_status(self):
        """
        :return:
        You have {total_workers_count} workers
        ----- {amount_of_keepers} Keepers:
        {keeper1}
        ...
        ----- {amount_of_caretakers} Caretakers:
        {caretaker1}
        ...
        ----- {amount_of_vetes} Vets:
        {vet1}
        ...
        Hint: use the __repr__ methods of the workers to print them on the console
        """
        pass
