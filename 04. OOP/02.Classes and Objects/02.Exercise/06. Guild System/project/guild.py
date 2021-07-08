from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            if player.guild == self.name:
                return f"Player {player.name} is already in the guild."
            else:
                return f"Player {player.name} is in another guild."
        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {player.guild}"

    def kick_player(self, player_name: str):
        if player_name in self.players:
            player_name.guild = "Unaffiliated"
            self.players.remove(player_name)
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for player in self.players:
            if player.guild == self.name:
                result += Player.player_info(player)
        return result
