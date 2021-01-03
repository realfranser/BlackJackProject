###IMPORTS###
import random

###ATRIBUTES###
# Suit codes
# Red suit -> red_suit % 2 = 0
hearts = 0
diamonds = 2
# Black suit -> black_suit % 2 = 1
spades = 1
clubs = 3
# Suit array, for showing card names cleaner
suit_array = ['hearts','spades','diamonds','clubs']


###CLASSES###
# Define object card
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def black_suit(self):
        return bool(self.suit % 2)
    def show(self):
        print("{} of {}".format(self.value, suit_array[self.suit]))

# Define object deck
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for s in [hearts, spades, diamonds, clubs]:
            for v in range(1,14):
                self.cards.append(Card(v, s))
    def show(self):
        for c in self.cards:
            c.show()
                        
# Define object shoe
class Shoe:
    def __init__(self, number_of_decks):
        self.cards = []
        self.number_of_decks = number_of_decks
        self.stacked_shoe = [[0]*4 for _ in range(1,14)]
        self.build()
        self.stack_cards()
    def build(self):
        for _ in range(self.number_of_decks):
            self.cards += Deck().cards
    def show(self):
        for c in self.cards:
            c.show()
    def shuffle(self):
        random.shuffle(self.cards)
    def stack_cards(self):
        for c in self.cards:
            self.stacked_shoe[c.value-1][c.suit]+=1
    # Use card function can be used for dealing it or for burning purposes, it depends if we want to use it or not
    def use_card(self):
        card =  self.cards.pop()
        self.stacked_shoe[card.value-1][card.suit]-=1
        return card

###FUNCTIONS###

