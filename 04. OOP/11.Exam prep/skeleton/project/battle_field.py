from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:
    Beginner_health_increment = 40
    Players_deck_card_increment = 30

    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")
        for player_type in (attacker, enemy):
            player_type.health += sum([
                player_deck_card.health_points for player_deck_card in player_type.card_repository.cards
            ])
            if type(player_type) is Beginner:
                player_type.health += BattleField.Beginner_health_increment
                for player_card in player_type.card_repository.cards:
                    player_card.damage_points += BattleField.Players_deck_card_increment
                    if player_type.is_dead:
                        return
                    player_type.take_damage(player_card.damage_points)
