import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def test_attr_are_set(self):
        magic_card = MagicCard('test')
        self.assertEqual(magic_card.name, 'test')
        self.assertEqual(magic_card.damage_points, 5)
        self.assertEqual(magic_card.health_points, 80)

    def test_name_raise_exemption_when_empty(self):
        with self.assertRaises(Exception) as ex:
            _ = MagicCard('')
        self.assertIsNotNone(ex.exception)

    def test_damage_point_raise_exemption_when_less_than_0(self):
        with self.assertRaises(Exception) as ex:
            magic_card = MagicCard('test')
            magic_card.damage_points = -5
        self.assertIsNotNone(ex.exception)

    def test_health_point_raise_exemption_when_less_than_0(self):
        with self.assertRaises(Exception) as ex:
            magic_card = MagicCard('test')
            magic_card.health_points = -5

        self.assertIsNotNone(ex.exception)


if __name__ == '__main__':
    unittest.main()
