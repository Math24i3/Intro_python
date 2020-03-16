import collections


# Card = collections.namedtuple('Card', ['rank', 'suit'])
# Card object
class Card(object):
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def __str__(self):
        return f'Rank: {self._rank}. Suit: {self._suit}'


# The deck of cards
class DeckOfCards(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    # Init
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    # Get the length of the deck
    def __len__(self):
        return len(self._cards)

    # Get a specific card
    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self):
        return self.__dict__

    def __str__(self):
        return str(self._cards)


newDeck = DeckOfCards()

for card in newDeck:
    print(card)

