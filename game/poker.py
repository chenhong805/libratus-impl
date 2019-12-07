# coding=utf-8
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__file__)

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
CARDS_RANK = range(2, 15) # 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A

ALL_CARDS = set()
for s in SUITS:
    for c in CARDS_RANK:
        ALL_CARDS.add(
            (c, s)
        )
