from abc import ABC, abstractmethod


class Library(ABC):
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    @abstractmethod
    def find_book(self):
        pass


class Book(Library):

    def find_book(self):
        pass

    def turn_page(self, page):
        self.page = page
