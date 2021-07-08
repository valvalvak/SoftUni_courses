class Player:
    players_list = []
    player_guild = "Unaffiliated"

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.players = Player.players_list
        self.guild = Player.player_guild

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        result = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
        result += "\n".join([f"==={key} - {val}" for key, val in self.skills.items()])
        # for key, val in self.skills.items():
        #     result += f"==={key} - {val}\n"
        return result


