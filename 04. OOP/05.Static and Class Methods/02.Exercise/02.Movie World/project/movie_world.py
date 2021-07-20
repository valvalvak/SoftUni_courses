from typing import List

from project.customer import Customer
from project.dvd import DVD


def is_dvd_rent_by_customer():
    pass


def is_customer_allowed_to_rent_dvd():
    pass


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List = []
        self.dvds: List = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if self.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if self.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        pass

    def reutn_dvd(self):
        pass

    def __repr__(self):
        pass
