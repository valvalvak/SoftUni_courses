from unittest import TestCase, main

from project.pet_shop import PetShop


class TestPetShop(TestCase):
    def setUp(self):
        self.name = PetShop("Bubba")

    def test_init_attribute(self):
        self.assertEqual(f"{self.name}", self.name)

    def test_add_food_successfully(self):
        added = self.name.add_food("Meat", 5)
        self.assertEqual("Successfully added 5.00 grams of Meat.", added)

    def test_add_pet_successfully(self):
        added = self.name.add_pet("Dudda")
        self.assertEqual("Successfully added Dudda.", added)

    def test_feed_pet_successfully(self):
        fed = self.name.feed_pet("Hills", "Lory")
        self.assertEqual(f"Lory was successfully fed", fed)

    def test_add_zero_food_rise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.name.add_food("Meat", -5)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ve.exception))

    def test_add_pet_with_same_name_raises_exception(self):
        self.name.add_pet("Bubba")
        with self.assertRaises(Exception) as ex:
            self.name.add_pet("Bubba")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_a_pet_not_in_list_rasies_exeption(self):
        with self.assertRaises(Exception) as ex:
            self.name.feed_pet("Hills", "Jojoba")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_a_pet_with_a_food_not_in_list_return_message(self):
        message = self.name.feed_pet("Jojoba", "Hills")
        self.assertEqual("You do not have Jojoba", message)


if __name__ == "__main__":
    main()
