from collections import deque

from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []
        self._message = "Successfully added: "

    @staticmethod
    def get_player_by_name(players, player_name):
        for player in players:
            if player.name == player_name:
                return player

    def add_player(self, *players_obj_que: Player):
        added = []
        for player in players_obj_que:
            if player not in self.players:
                self.players.append(player)
                added.append(player.name)
        if added:
            return self._message + ', '.join(name for name in added)
        return self._message

    def add_supply(self, *supply_obj_que: Supply):
        for obj in supply_obj_que:
            self.supplies.append(obj)

    def sustain(self, player_name: str, sustenance_type: str):
        supply = {
            'name': None,
            'energy': None,
            'index': None,
        }
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == sustenance_type:
                supply['name'] = self.supplies[i].name
                supply['energy'] = self.supplies[i].energy
                supply['index'] = i
                break

        player = self.get_player_by_name(self.players, player_name)
        player.stamina += supply['energy']

        if supply['index'] is not None:
            self.supplies.remove(self.supplies[supply['index']])

        return f"{player_name} sustained successfully with {supply['name']}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self.get_player_by_name(self.players, first_player_name)
        player2 = self.get_player_by_name(self.players, second_player_name)
        duel_stack = [player1, player2]
        duel_queue = deque(duel_stack)
        counter = 0
        while counter < 2:
            attacker = duel_queue.popleft()
            defender = duel_queue.popleft()
            if attacker.stamina == 0:
                return f"Player {attacker.name} does not have enough stamina."
            elif all(duel_stack) == 0:
                message = '\n'.join(f"Player {p.name} does not have enough stamina." for p in duel_stack)
                return message
            if attacker.stamina > defender.stamina:
                duel_queue.append(defender)
                duel_queue.append(attacker)
                continue
            defender.stamina -= attacker.stamina / 2
            duel_queue.append(defender)
            duel_queue.append(attacker)
            if defender.stamina <= 0:
                defender.stamina = 0
                return f"Winner: {attacker.name}"
            counter += 1
        return f"Winner: {player1.name if player1.stamina > player2.stamina else player2.name}"

    def next_day(self):
        for player in self.players:
            player.stamina -= player.age * 2
            if player.stamina < 0:
                player.stamina = 0
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')
