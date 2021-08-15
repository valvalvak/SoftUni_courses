import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def test_attr_are_set(self):
        trap_card = TrapCard('test')
        self.assertEqual(trap_card.name, 'test')
        self.assertEqual(trap_card.damage_points, 120)
        self.assertEqual(trap_card.health_points, 5)

    def test_name_raise_exemption_when_empty(self):
        with self.assertRaises(Exception) as ex:
            _ = TrapCard('')
        self.assertIsNotNone(ex.exception)

    def test_damage_point_raise_exemption_when_less_than_0(self):
        with self.assertRaises(Exception) as ex:
            trap_card = TrapCard('test')
            trap_card.damage_points = -5
        self.assertIsNotNone(ex.exception)

    def test_health_point_raise_exemption_when_less_than_0(self):
        with self.assertRaises(Exception) as ex:
            trap_card = TrapCard('test')
            trap_card.health_points = -5
        self.assertIsNotNone(ex.exception)


if __name__ == '__main__':
    unittest.main()
