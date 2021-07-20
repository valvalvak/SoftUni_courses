# from math import floor
#
# from project.dough import Dough
# from project.topping import Topping
#
#
# class Pizza:
#     def __init__(self, name: str, dough: Dough, toppings_capacity: int, toppings: dict):
#         self.name = name
#         self.dough = dough
#         self.toppings_capacity = toppings_capacity
#         self.toppings = toppings
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if len(value) < 1:
#             raise ValueError("The name cannot be an empty string")
#         self.__name = value
#
#     @property
#     def dough(self):
#         return self.__dough
#
#     @dough.setter
#     def dough(self, value):
#         if value is None:
#             raise ValueError("You should add dough to the pizza")
#         self.__dough = value
#
#     @property
#     def topping_capacity(self):
#         return self.__toppings_capacity
#
#     @topping_capacity.setter
#     def topping_capacity(self, value):
#         if value < 1:
#             raise ValueError("The topping's capacity cannot be less or equal to zero")
#         self.__toppings_capacity = value
#
#     def add_topping(self, topping: Topping):
#         pass
#
#     def calculate_total_weight(self):
#         pass
from math import floor

a = round(5.4999999999999995)
b = round(5.4999999999999996)
c = floor(5.4999999999999995)
d = floor(5.4999999999999996)

print(a, b, c, d)
