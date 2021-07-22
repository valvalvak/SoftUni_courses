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

    @staticmethod
    def get_dvd(dvd_id, dvds_list):
        dvd = [x for x in dvds_list if x.id == dvd_id]
        if len(dvd) > 0:
            return dvd[0]

    @staticmethod
    def get_customer(customer_id, customers_list):
        customer = [x for x in customers_list if x.id == customer_id]
        if len(customer) > 0:
            return customer[0]

    @staticmethod
    def is_dvd_rented(dvd, rented_dvds):
        if dvd in rented_dvds:
            return True
        return False

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = self.get_dvd(dvd_id, self.dvds)
        customer = self.get_customer(customer_id, self.customers)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        elif dvd not in customer.rented_dvds:
            if dvd.is_rented:
                return "DVD is already rented"
            elif dvd.age_restriction > customer.age:
                return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
            else:
                customer.rented_dvds.append(dvd)
                dvd.is_rented = True
                return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        dvd = self.get_dvd(dvd_id, self.dvds)
        customer = self.get_customer(customer_id, self.customers)
        if self.is_dvd_rented(dvd, customer.rented_dvds):
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += repr(customer) + '\n'
        for dvd in self.dvds:
            result += repr(dvd) + '\n'
        return result.rstrip('\n')
