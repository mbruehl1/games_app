from random import Random

class Cards:
    """ TEXT"""

    def __init__(self):
        """ Create deck of cards:"""
        self.deck = { 'Diamonds' : ['A',2,3,4,5,6,7,8,9,10,'J','Q','K'],
                      'Hearts'   : ['A',2,3,4,5,6,7,8,9,10,'J','Q','K'],
                      'Spades'   : ['A',2,3,4,5,6,7,8,9,10,'J','Q','K'],
                      'Clubs'    : ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']}
        self.card = None
        self.my_rand = Random()

    def draw(self):
        """ Draw a card from suit/value and return the value"""
        suit  = self.my_rand.sample(self.deck.keys(), 1)[0]
        value = str(self.deck[suit][int(13 * self.my_rand.random())])
        self.card = value + "-" + suit
        return self.card
