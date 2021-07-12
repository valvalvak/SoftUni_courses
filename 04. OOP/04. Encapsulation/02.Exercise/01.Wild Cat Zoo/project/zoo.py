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
        if self.__budget < price:
            return "Not enough budget"
        elif self.__animal_capacity < len(self.animals) + 1:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__worker_capacity < len(self.workers) + 1:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salaries_sum = sum([worker.salary for worker in self.workers])
        if self.__budget >= workers_salaries_sum:
            self.__budget -= workers_salaries_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_to_tend_all_animals = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= sum_to_tend_all_animals:
            self.__budget -= sum_to_tend_all_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

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
