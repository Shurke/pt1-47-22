# You get any card as an argument. Your task is to return a suit of this card.

# Our deck (is preloaded)

def define_suit(card):
    if card[-1] == 'S':
        return 'spades'
    elif card[-1] == 'D':
        return 'diamonds'
    elif card[-1] == 'H':
        return 'hearts'
    else:
        return 'clubs'
