from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers: List = []
        self.dvds: List = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if self.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if self.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = list(map(lambda x: x.id == dvd_id, self.dvds))
        customer = list(map(lambda x: x.id == customer_id, self.customers))
        if len(dvd) > 0:
            dvd = dvd[0]
        if len(customer) > 0:
            customer = customer[0]
        if dvd in Customer.get_rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd not in Customer.get_rented_dvds:
            if dvd.is_ranted:
                return "DVD is already rented"
            elif dvd.age_restriction > customer.age:
                return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
            else:

                Customer.add_rented_dvds(dvd)




            pass

    def return_dvd(self):
        pass

    def __repr__(self):
        pass
