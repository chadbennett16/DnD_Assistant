from random import randint

class Dice(object):
    """description of class"""
    def __init__(self, sides):
        self.sides = "sides"

    def dice_roll(self, sides):
        return randint(1, sides)
    
    # For percentile, call dice_roll(1,10) * 10
    
