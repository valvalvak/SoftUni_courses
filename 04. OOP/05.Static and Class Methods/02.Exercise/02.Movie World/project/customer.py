from typing import List


class Customer:
    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds: List = []

    def __repr__(self):
        dvds_count = len(self.rented_dvds)
        repr_dvd_list = ', '.join([x for x in self.rented_dvds])
        result = f"{self.id}: {self.name} of age {self.age} has {dvds_count} rented DVD's ({repr_dvd_list})"
        return result
