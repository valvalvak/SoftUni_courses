from typing import List

from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu: List = []
        self.drinks_menu: List = []
        self.tables_repository: List = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or set(value) == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        food_order = None
        if food_type == "Bread":
            food_order = Bread(name, price)
        elif food_type == "Cake":
            food_order = Cake(name, price)
        for ordering_food in self.food_menu:
            if ordering_food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")
        if food_order:
            self.food_menu.append(food_order)
            str_res = f"Added {name} ({food_type}) to the food menu"
            return str_res

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        drink_order = None
        if drink_type == "Tea":
            drink_order = Tea(name, portion, brand)
        elif drink_type == "Cake":
            drink_order = Water(name, portion, brand)
        for ordering_food in self.food_menu:
            if ordering_food.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_order:
            self.drinks_menu.append(drink_order)
            str_res = f"Added {name} ({brand}) to the drink menu"
            return str_res

    def add_table(self, table_type: str, table_number: int, capacity: int):
        table = None
        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)
        for if_table_in_bakery in self.tables_repository:
            if if_table_in_bakery.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")
        if table:
            self.tables_repository.append(table)
            str_res = f"Added table number {table_number} in the bakery"
            return str_res

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and number_of_people <= table.capacity:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_name: str):
        for table in self.tables_repository:
            if table.table_number == table_number:
                self.food_menu.extend(food_name)
                return
        return f"Could not find table {table_number}"

    def order_drink(self, table_number: int, *drink_name: str):
        for table in self.tables_repository:
            if table.table_number == table_number:
                self.drinks_menu.extend(drink_name)

    def leave_table(self, table_number: int):
        pass
