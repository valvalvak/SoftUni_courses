class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"
        self.players = []

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return "Skill {skill_name} added to the collection of the player {player_name}"

    @staticmethod
    def player_info():
        return repr(Player)

    def __repr__(self):
        print(f"{self.name}")
        print(f"{self.guild}")
        print(f"HP:{self.hp}")
        print(f"HP:{self.mp}")
        for key, val in self.skills.items():
            print(f"==={key} - {val}")
