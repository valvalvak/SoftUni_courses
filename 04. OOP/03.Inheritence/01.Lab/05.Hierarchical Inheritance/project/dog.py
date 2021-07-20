from project.animal import Animal


class Dog(Animal):
    def __init__(self):
        super(Animal).__init__()

    @staticmethod
    def bark():
        return "barking..."
