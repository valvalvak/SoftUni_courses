from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        for searched_player in self.players:
            if searched_player.username == player.username:
                raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count = len(self.players)

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        for playa in self.players:
            if playa.username == player:
                self.players.remove(playa)
                self.count = len(self.players)

    def find(self, username: str):
        for playa in self.players:
            if playa.username == username:
                return playa
