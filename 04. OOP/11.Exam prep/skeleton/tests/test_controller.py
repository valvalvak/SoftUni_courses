import unittest

from project.card.card_repository import CardRepository
from project.controller import Controller
from project.player.player_repository import PlayerRepository


class TestController(unittest.TestCase):
    def setUp(self) -> None:
        self.player_repo = PlayerRepository()
        self.card_repository = CardRepository()
        self.controller = Controller()

    def test_adding_new_player(self):
        result = self.controller.add_player('Beginner', 'test')
        self.assertEqual(result, "Successfully added player of type Beginner with username: test")

    def test_adding_new_card(self):
        result = self.controller.add_card('Trap', 'test')
        self.assertEqual(result, "Successfully added card of type TrapCard with name: test")


if __name__ == '__main__':
    unittest.main()
