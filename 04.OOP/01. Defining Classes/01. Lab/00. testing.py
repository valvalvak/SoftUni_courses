class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_older(self):
        self.age += 1

    def __str__(self):
        return f"{self.name}; {self.age}"


Peter = Person("Peter", 15)
Ivan = Person("Ivan", 20)

print(Peter)
print(Ivan)
Peter.get_older()
Ivan.get_older()
print(Peter)
print(Ivan)
