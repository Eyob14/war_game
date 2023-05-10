import random
from card import Card


class Deck:

    def __init__(self):
        self.ranks = ["2", "3", "4", "5", "6", "7", "8",
                      "9", "10", "Jack", "Queen", "King", "Ace"]
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.jokers = ["Joker", "Joker"]
        self.cards = []
        self.build()

    def build(self):
        for suit in self.suits:
            for rank in self.ranks:
                card = Card(rank, suit)
                self.cards.append(card)

        for joker in self.jokers:
            joker = Card(joker, "Joker")
            self.cards.append(joker)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()
