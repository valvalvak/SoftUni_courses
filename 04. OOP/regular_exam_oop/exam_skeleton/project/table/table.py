from abc import ABC, abstractmethod
from typing import List

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: List = []
        self.drink_orders: List = []
        self.number_of_people = 0
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, people_count: int):
        self.number_of_people = people_count
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        bill = 0
        for food in self.food_orders:
            bill += food.price
        for drink in self.drink_orders:
            bill += drink.price
        return bill

    def clear(self):
        for _ in self.food_orders:
            _.number_of_people = 0
        self.food_orders.clear()
        for _ in self.drink_orders:
            _.number_of_people = 0
        self.drink_orders.clear()

    def free_table_info(self):
        if self.is_reserved is False:
            str_res = f"Table: {self.table_number}\nType: {type(Table)}\nCapacity: {self.capacity}"
            return str_res
