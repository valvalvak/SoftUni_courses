from project.cat import Cat
from project.kitten import Kitten

if __name__ == '__main__':
    cat = Cat("boo", 5, "girl")
    kitten = Kitten("bo-bo", 1)
    print(cat.make_sound())
    print(kitten)
