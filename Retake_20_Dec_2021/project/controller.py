class Controller:
    def __int__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *player_obj_list):
        for player in player_obj_list:
            for pname in self.players:
                if pname.name == player.name:
                    raise Exception(f"Name {player.name} is already used!")
                self.players.append(player)

    def add_supply(self, supplys_obj_list):
        for obj in supplys_obj_list:
            for supply_type in self.supplies:
                if not obj.name == supply_type.name:
                    self.supplies.append(obj)

    def sustain(self, player_name: str, sustenance_type: str):
        pass

    def duel(self, first_player_name: str, second_player_name: str):
        pass

    def next_day(self):
        pass
