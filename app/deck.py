import random as rnd

DECK52 = []
SUITS = 'cdhs' # clubs, diamonds, hearts, spades
RANKS = '23456789tjdka' # t = ten

for s in SUITS:
    for r in RANKS:
        DECK52.append(f'{s}{r}')

class Deck:
    def __init__(self):
        self.init()

    def init(self):
        self.cards = DECK52.copy()

    def shuffle(self):
        rnd.shuffle(self.cards)

    def pop(self):
        result = None
        if len(self.cards) > 0:
            result = self.cards.pop()
        return result

    def pick(self):
        result = None
        if len(self.cards) > 0:
            result = self.cards[rnd.randint(0, len(self.cards))]
        return result

    def push(self, card):
        result = False
        if card not in self.cards:
            self.append(card)
            result = True
        return result

    def is_empty(self):
        return len(self.cards) < 1

