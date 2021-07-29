from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        pass


class Dog(Animal):

    def make_sound(self):
        return "Woof!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}"


class Cat(Animal):

    def make_sound(self):
        return "Meow meow!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}"


class Kitten(Cat):
    def __init__(self, name, age, gender="Female"):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Meow"


class Tomcat(Cat):
    def __init__(self, name, age, gender="Male"):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Hiss"
