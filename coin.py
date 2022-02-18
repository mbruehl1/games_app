from random import Random

class Coin:
    """ TEXT"""

    def __init__(self):
        """ Create coin object: Initalize the coin flip value"""
        self.value = None
        self.my_rand = Random()

    def flip(self):
        """ Flip the coin and return the value:"""
        if self.my_rand.random()<0.5:
            self.value = "HEADS"
        else:
            self.value = "TAILS"
        return self.value
