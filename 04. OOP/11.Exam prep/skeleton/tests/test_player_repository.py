import unittest

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def test_attr_are_set(self):
        player_repository = PlayerRepository()
        self.assertEqual(player_repository.count, 0)
        self.assertEqual(player_repository.players, [])

    def test_add_method_raise_ex_when_card_already_exist(self):
        with self.assertRaises(Exception) as ex:
            player_repository = PlayerRepository()
            beginner = Beginner('test')
            player_repository.add(beginner)
            player_repository.add(beginner)
        self.assertIsNotNone(ex.exception)

    def test_add_method_add_card_when_unique(self):
        player_repository = PlayerRepository()
        beginner = Beginner('test')
        beginner2 = Beginner('test2')
        player_repository.add(beginner)
        player_repository.add(beginner2)
        self.assertEqual(2, player_repository.count)

    def test_remove_method_remove_card(self):
        player_repository = PlayerRepository()
        beginner = Beginner('test')
        player_repository.add(beginner)
        player_repository.remove('test')

    def test_find_card_method(self):
        player_repository = PlayerRepository()
        beginner = Beginner('test')
        player_repository.add(beginner)
        player_repository.find('test')


if __name__ == '__main__':
    unittest.main()
