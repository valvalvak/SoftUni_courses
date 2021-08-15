import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def test_attr_are_set(self):
        card_repository = CardRepository()
        self.assertEqual(card_repository.count, 0)
        self.assertEqual(card_repository.cards, [])

    def test_add_method_raise_ex_when_card_already_exist(self):
        with self.assertRaises(Exception) as ex:
            card_repository = CardRepository()
            magic_card_1 = MagicCard('test')
            card_repository.add(magic_card_1)
            card_repository.add(magic_card_1)
        self.assertIsNotNone(ex.exception)

    def test_add_method_add_card_when_unique(self):
        card_repository = CardRepository()
        magic_card_1 = MagicCard('test')
        magic_card_2 = MagicCard('test2')
        card_repository.add(magic_card_1)
        card_repository.add(magic_card_2)
        self.assertEqual(2, card_repository.count)

    def test_remove_method_remove_card(self):
        card_repository = CardRepository()
        magic_card_1 = MagicCard('test')
        card_repository.add(magic_card_1)
        card_repository.remove('test')

    def test_find_card_method(self):
        card_repository = CardRepository()
        magic_card_1 = MagicCard('test')
        card_repository.add(magic_card_1)
        card_repository.find('test')


if __name__ == '__main__':
    unittest.main()
