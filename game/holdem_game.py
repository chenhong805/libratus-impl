from game.poker import ALL_CARDS


class Player(object):
    def __init__(self, name, chip_val):
        self.name = name
        self.chip_val = chip_val


class Dealer(object):
    def __init__(self, name):
        self.name = name
        self.cards = set(ALL_CARDS)


class Pot(object):
    def __init__(self, chip_val):
        self.chip_val = chip_val


class CommunityCards(object):
    def __init__(self, cards):
        self.cards = set(cards)

    def add(self, card):
        self.cards.add(card)


class Round(object):
    def __init__(self, name):
        self.name = name


class Game(object):
    def __init__(self, players, dealer):
        self.players = players
        self.dealer = dealer