class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int, ):
        self.name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        nl = "\n"
        print_result = f"Player: {self.__name}{nl}"
        print_result += f"Sprint: {self.__sprint}{nl}"
        print_result += f"Dribble: {self.__dribble}{nl}"
        print_result += f"Passing: {self.__passing}{nl}"
        print_result += f"Shooting: {self.__shooting}"
        return print_result
