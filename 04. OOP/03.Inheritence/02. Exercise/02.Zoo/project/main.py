from project.gorilla import Gorilla
from project.lizard import Lizard
from project.mammal import Mammal

if __name__ == '__main__':
    mammal = Mammal("Stella")
    print(mammal.__class__.__bases__[0].__name__)
    print(mammal.name)
    lizard = Lizard("John")
    print(lizard.__class__.__bases__[0].__name__)
    print(lizard.name)
    gorilla = Gorilla("Kong")
    print(gorilla.name)
    print(gorilla.__class__.__bases__[0].__name__)
