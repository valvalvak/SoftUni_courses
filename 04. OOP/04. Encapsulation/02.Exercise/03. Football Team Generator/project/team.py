from typing import List

from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List = []

    def add_player(self, player: Player):
        if not [pl for pl in self.__players if pl.name == player.name]:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"
        return f"Player {player.name} has already joined"

    def remove_player(self, player_name: str):
        if not [pl for pl in self.__players if pl.name == player_name]:
            return f"Player {player_name} not found"
        obj = [obj for obj in self.__players if obj.name == player_name]
        self.__players.remove(obj[0])
        return obj[0]
