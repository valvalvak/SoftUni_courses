class Planet:
    def __init__(self, name: str, items):
        self.name = name
        self.items = [items]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        empty_str = ""
        whitespace = set(" ")
        if value == empty_str or value == whitespace:
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value
