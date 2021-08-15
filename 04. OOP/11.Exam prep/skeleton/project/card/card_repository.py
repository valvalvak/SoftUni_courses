from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        for card_obj in self.cards:
            if card_obj.name == card.name:
                raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count = len(self.cards)

    def remove(self, card: str):
        if card == "":
            raise ValueError()
        for searched_card in self.cards:
            if searched_card.name == card:
                self.cards.remove(searched_card)
                self.count = len(self.cards)

    def find(self, name: str):
        for searched_card_obj in self.cards:
            if searched_card_obj.name == name:
                return searched_card_obj
