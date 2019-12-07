# coding=utf-8
from misc import get_logger
logger = get_logger(__file__)

SPADE = '♠'
HEART = '♥'
CLUB = '♣'
DIAMOND = '♦'

SUITS_RANK = {
    # higher is better
    SPADE: 3,
    HEART: 2,
    CLUB: 1,
    DIAMOND: 0
}

SUITS = [SPADE, HEART, CLUB, DIAMOND]
# 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
CARDS_RANK = range(2, 15)

ALL_CARDS = set()
for s in SUITS:
    for c in CARDS_RANK:
        ALL_CARDS.add(
            (c, s)
        )
