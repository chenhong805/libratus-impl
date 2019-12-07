from game.poker import ALL_CARDS

import random


class Player(object):
    def __init__(self, name, chip_val, private_cards=None):
        self.name = name
        self.chip_val = chip_val
        self.private_cards = private_cards

    def receive_private_cards(self, private_cards):
        self.private_cards = private_cards

    def decide_small_blind(self, game):
        return random.randint(1, self.chip_val)

    def decide_big_blind(self, game):
        return random.randint(1, self.chip_val)

    def place_bet(self, val):
        self.chip_val -= val


class Dealer(object):
    def __init__(self, name):
        self.name = name
        self.cards = list(ALL_CARDS)
        self.community_cards = []

    def draw_random_cards(self, num):
        n = num
        r = []
        while n > 0:
            r.append(self.cards[random.randint(0, len(self.cards))])
            n -= 1
        return r


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
    def __init__(self, players, dealer, pot):
        # in order
        self.players = players
        self.dealer_button_at = -1
        self.dealer = dealer
        self.pot = Pot(0)

    def first_actor(self):
        return (self.dealer_button_at + 3) % len(self.players)

    def shuffle_dealer_button(self):
        # do we need this? to change the order and dealer button, check the rules
        pass

    def place_small_blind(self):
        val = self.players[0].decide_small_blind(self)
        self.players[0].place_bet(val)

    def place_big_blind(self):
        val = self.players[0].decide_small_blind(self)
        self.players[0].place_bet(val)

    def init_pre_flop(self):

        self.place_small_blind()
        self.place_big_blind()

        community_cards = self.dealer.draw_random_cards(3)
        self.dealer.community_cards = community_cards

        for p in self.players:
            private_cards = self.dealer.draw_random_cards(2)
            p.private_cards = private_cards

    def init_flop(self):
        pass

    def init_turn(self):
        pass

    def init_river(self):
        pass

    def init_showdown(self):
        pass

    def play(self):
        pass
