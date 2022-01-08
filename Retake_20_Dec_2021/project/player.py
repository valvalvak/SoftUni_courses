class Player:

    _added_players_names = []

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.need_sustenance = bool

    @staticmethod
    def is_duplicated_player(player_name, added_players):
        if player_name in added_players:
            return True
        return False

    @property
    def needs_sustenance(self):
        return self.stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        player_name = value.strip()
        if player_name == "":
            raise ValueError("Name not valid!")
        elif self.is_duplicated_player(player_name, Player._added_players_names):
            raise Exception(f"Name {player_name} is already used!")
        else:
            Player._added_players_names.append(player_name)
        self.__name = player_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if 0 > value > 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value
