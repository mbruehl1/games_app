from random import Random

class Dice:
    """ TEXT"""

    def __init__(self):
        """ Create dice object: Initalize the roll value"""
        self.value = None
        self.my_rand = Random()

    def roll(self):
        """ Roll the dice and return the value"""
        self.value = 1 + int(6 * self.my_rand.random())
        return self.value

