from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: object):
        self.products.append(product)

    def find(self, product_name: str):
        obj = [obj for obj in self.products if obj.name == product_name]
        return obj

    def remove(self, product_name):
        product = [prod for prod in self.products if prod.name == product_name]
        if product and self.products:
            self.products.remove(product[0])

    def __repr__(self):
        return "\n".join([f"{prd.name}: {prd.quantity}" for prd in self.products])

