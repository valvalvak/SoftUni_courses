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

    @staticmethod
    def __str_obj_output(class_name, objects):
        print_output = "\n".join([f"{repr(obj)}" for obj in objects if type(obj).__name__ == class_name]) + "\n"
        return print_output

    @staticmethod
    def __count_amount(class_name, objects):
        amount = sum(map(lambda x: type(x).__name__ == class_name, objects))
        return amount

    def animals_status(self):
        animals_print_order = (
            ("Lion", "Lions"),
            ("Tiger", "Tigers"),
            ("Cheetah", "Cheetahs"),
        )

        print_output = f"You have {len(self.animals)} animals\n"

        for (class_name, names) in animals_print_order:
            amount = self.__count_amount(class_name, self.animals)
            print_output += f"----- {amount} {names}:" + "\n"
            print_output += self.__str_obj_output(class_name, self.animals)

        return print_output.rstrip("\n")

    def workers_status(self):
        workers_print_order = (
            ("Keeper", "Keepers"),
            ("Caretaker", "Caretakers"),
            ("Vet", "Vets"),
        )

        print_output = f"You have {len(self.workers)} workers\n"

        for class_name, names in workers_print_order:
            amount = self.__count_amount(class_name, self.workers)
            print_output += f"----- {amount} {names}:" + "\n"
            print_output += self.__str_obj_output(class_name, self.workers)

        return print_output.rstrip("\n")

# def animals_status(self):
#         result = [f"You have {len(self.animals)} animals"]
#
#         lions = [a.__repr__() for a in self.animals if a.__class__.__name__ == "Lion"]
#         result.extend([f"----- {len(lions)} Lions:"])
#         result.extend(lions)
#
#         tigers = [a.__repr__() for a in self.animals if a.__class__.__name__ == "Tiger"]
#         result.extend([f"----- {len(tigers)} Tigers:"])
#         result.extend(tigers)
#
#         cheetahs = [a.__repr__() for a in self.animals if a.__class__.__name__ == "Cheetah"]
#         result.extend([f"----- {len(cheetahs)} Cheetahs:"])
#         result.extend(cheetahs)
#
#         return "\n".join(result)
