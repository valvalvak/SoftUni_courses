from unittest import TestCase, main

from project.library import Library


class TestLibrary(TestCase):
    def setUp(self):
        self.lib = Library("Test")

    def test_init(self):
        self.assertEqual("Test", self.lib.name)
        self.assertEqual({}, self.lib.books_by_authors)
        self.assertEqual({}, self.lib.readers)

    def test_add_invalid_name(self):
        with self.assertRaises(ValueError) as ex:
            self.lib.name("")
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book_to_dict(self):
        self.assertEqual({}, self.books_by_authors)
        self.lib.add_book("Stephen King", ["It"])
        self.assertEqual({"Stephen King": ["It"]}, self.lib.books_by_authors)
        self.lib.add_book("Stephen King", ["The Green Mile"])
        self.assertEqual({"Stephen King": ["It", "The Green Mile"]}, self.lib.books_by_authors)

    def test_add_reader(self):
        self.assertEqual({}, self.readers)
        self.lib.add_reader("Vako")
        self.assertEqual({"Vako": []}, self.lib.readers)

    def test_add_reader_already_registered(self):
        self.assertEqual({}, self.readers)
        self.lib.add_reader("Vako")
        self.assertEqual({"Vako": []}, self.lib.readers)
        result = self.lib.add_reader("Vako")
        self.assertEqual("Vako is already registered in the 'Test' library.", result)

    def test_rent_a_book_reader_not_in_library(self):
        self.assertEqual({}, self.readers)
        result = self.lib.rent_book("Test_reader_name", "test_book_author", "test_book_title")
        self.assertEqual("Test_reader_name is not registered in the Test Library.", result)

    def test_rent_a_book_author_not_in_library(self):
        self.assertEqual({}, self.books_by_authors)
        result = self.lib.rent_book("Test_reader_name", "test_book_author", "test_book_title")
        self.assertEqual("Test Library does not have any test_book_author's books.", result)

    def test_rent_a_book_title_not_in_library(self):
        self.assertEqual({"Vako": []}, self.readers)
        self.assertEqual({"Stephen King": ["It"]}, self.books_by_authors)
        result = self.lib.rent_book("Vako", "Stephen King", "The Green Mile")
        self.assertEqual("""Test Library does not have Stephen King's "The Green Mile".""", result)

    def test_rent_a_book_successes(self):
        self.assertEqual({"Vako": []}, self.readers)
        self.assertEqual({"Stephen King": ["It"]}, self.books_by_authors)
        self.lib.rent_book("Vako", "Stephen King", "It")
        self.assertEqual({"Vako": [{"Stephen King": "It"}]}, self.readers)
        self.assertEqual({}, self.books_by_authors)


if __name__ == '__main__':
    main()
