from game.poker import ALL_CARDS, SUITS_RANK

STRAIGHT_FLUSH = 'straight flush'
FOUR_OF_A_KIND = 'four of a kind'
FULL_HOUSE = 'full house'
FLUSH = 'flush'
STRAIGHT = 'straight'
THREE_OF_A_KIND = 'three of a kind'
TWO_PAIR = 'two pair'
PAIR = 'pair'
HIGH_CARD = 'high card'

HANDS_RANK = {
    # higher is better
    # ROYAL_FLUSH: 9,
    STRAIGHT_FLUSH: 8,
    FOUR_OF_A_KIND: 7,
    FULL_HOUSE: 6,
    FLUSH: 5,
    STRAIGHT: 4,
    THREE_OF_A_KIND: 3,
    TWO_PAIR: 2,
    PAIR: 1,
    HIGH_CARD: 0,
}

def is_straight_flush(h):
    suits = set()
    for c in h:
        suits.add(c[1])
    if len(suits) > 1:
        return None
    suit = None
    for ss in suits:
        suit = ss
        break

    h0 = sorted(h, key=lambda x: x[0])
    for i in range(1, len(h0)):
        if h0[i][0] - h0[i-1][0] != 1:
            return None

    return {
        'rank': STRAIGHT_FLUSH,
        'suit': suit,
        'max_card': h0[-1]
    }

def is_four_of_a_kind(h):
    card_ranks_count = {}
    for c in h:
        if c[0] in card_ranks_count:
            card_ranks_count[c[0]] += 1
        else:
            card_ranks_count[c[0]] = 1

    for k in card_ranks_count.keys():
        if card_ranks_count[k] == 4:
            return {
                'rank' : FOUR_OF_A_KIND,
                'card_rank': k,
            }
    return None

def is_full_house(h):
    card_ranks_count = {}
    for c in h:
        if c[0] in card_ranks_count:
            card_ranks_count[c[0]].add(c)
        else:
            card_ranks_count[c[0]] = {c}

    three_of_a_kind = None
    pair = None

    for k in card_ranks_count.keys():
        if len(card_ranks_count[k]) == 3:
            three_of_a_kind = {
                'card_rank': k,
            }
        if len(card_ranks_count[k]) == 2:
            pair = {
                'card_rank': k,
                'max_suit': sorted(
                    list(card_ranks_count[k]), key=lambda c: SUITS_RANK[c[1]]
                )[-1]
            }
    if three_of_a_kind and pair:
        return {
            'rank': FULL_HOUSE,
            'three_of_a_kind': three_of_a_kind,
            'pair': pair
        }
    return None

def is_flush(h):
    suits = set()
    for c in h:
        suits.add(c[1])
    if len(suits) == 1:
        return {
            'rank': FLUSH,
            # TODO: need to handle aces
            'max_card': sorted(list(h), key=lambda c: c[0] * 10 + SUITS_RANK[c[1]])[-1]
        }
    return None

def is_straight(h):

    h0 = sorted(h, key=lambda x: x[0])
    for i in range(1, len(h0)):
        if h0[i][0] - h0[i-1][0] != 1:
            return None

    return {
        'rank': STRAIGHT,
        'max_card': h0[-1]
    }

def is_three_of_a_kind(h):
    card_ranks_count = {}
    for c in h:
        if c[0] in card_ranks_count:
            card_ranks_count[c[0]].add(c)
        else:
            card_ranks_count[c[0]] = {c}

    for k in card_ranks_count.keys():
        if len(card_ranks_count[k]) == 3:
            three_of_a_kind = {
                'card_rank': k,
            }
            return {
                'rank': THREE_OF_A_KIND,
                'card_rank': k
            }
    return None

def is_two_pair(h):
    card_ranks_count = {}
    for c in h:
        if c[0] in card_ranks_count:
            card_ranks_count[c[0]].add(c)
        else:
            card_ranks_count[c[0]] = {c}

    pair0 = None
    pair1 = None

    for k in card_ranks_count.keys():
        if len(card_ranks_count[k]) == 2:
            if not pair0:
                pair0 = {
                    'max_card': sorted(list(card_ranks_count[k]), key=lambda c: c[0] * 10 + SUITS_RANK[c[1]])[-1],
                }
            else:
                pair1 = {
                    'max_card': sorted(list(card_ranks_count[k]), key=lambda c: c[0] * 10 + SUITS_RANK[c[1]])[-1],
                }
    if pair0 and pair1:
        return {
            'rank': TWO_PAIR,
            'pair0': pair0,
            'pair1': pair1
        }

    if pair0:
        return {
            'rank': PAIR,
            'pair': pair0,
        }
    return None

def is_high_card(h):
    return {
        'rank': HIGH_CARD,
        'max_card': sorted(list(h), key=lambda c: c[0] * 10 + SUITS_RANK[c[1]])[-1]
    }


def detect_hands_type(h):
    detectors = [
        is_straight_flush,
        is_four_of_a_kind,
        is_full_house,
        is_flush,
        is_straight,
        is_three_of_a_kind,
        is_two_pair,
        is_high_card
    ]
    for d in detectors:
        r = d(h)
        if r:
            return r

def compare_card(c0, c1):
    c00 = c0[0] * 10 + SUITS_RANK[c0[1]]
    c11 = c1[0] * 10 + SUITS_RANK[c1[1]]
    return c00 - c11

def max_cards(cards):
    return sorted(cards, key=lambda x: x[0] * 10 + SUITS_RANK[x[1]])[-1]

def compare_hands(h0, h1):
    ht0 = detect_hands_type(h0)
    ht1 = detect_hands_type(h1)
    if HANDS_RANK[ht0['rank']] > HANDS_RANK[ht1['rank']]:
        return 1
    elif HANDS_RANK[ht0['rank']] < HANDS_RANK[ht1['rank']]:
        return -1
    else:# HANDS_RANK[ht0['rank']] == HANDS_RANK[ht1['rank']]:
        if 'max_card' in ht0:
            return compare_card(
                ht0['max_card'],
                ht1['max_card'],
            )
        if 'card_rank' in ht0:
            return ht0['card_rank'] - ht1['card_rank']
        if 'three_of_a_kind' in ht0:
            return ht0['three_of_a_kind']['card_rank'] - ht1['three_of_a_kind']['card_rank']
        if TWO_PAIR == ht0['rank']:
            p00 = ht0['pair0']['max_card']
            p01 = ht0['pair1']['max_card']
            p0_max = max_cards([p00, p01])
            p10 = ht1['pair0']['max_card']
            p11 = ht1['pair1']['max_card']
            p1_max = max_cards([p10, p11])
            return compare_card(p0_max, p1_max)
        if PAIR == ht0['rank']:
            p00 = ht0['pair']['max_card']
            p10 = ht1['pair']['max_card']
            return compare_card(p00, p10)

    raise ValueError('shouldn\'t occur')

HAND_SIZE = 5

TOTAL_POSSIBLE_HANDS = 52 * 51 * 50 * 49 * 48