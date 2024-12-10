import random

from ascii_images import ascii_sides
from enum import Enum

class DiceType(Enum):
    D20 = 20
    D16 = 16
    D12 = 12
    D10 = 10
    D8 = 8
    D6 = 6
    D4 = 4

class Dice:
    def __init__(self):
        self.dice_type = None
        self.sides = None
        self.rolls = []
        self.current_roll = None
        self.ascii = None

    def roll(self) -> int:
        """Rolls the Die"""
        self.current_roll = random.randint(1, self.dice_type.value)
        self.rolls.append(self.current_roll)
        self.ascii = ascii_sides[self.dice_type.value][self.current_roll]
        print(self.ascii)
        return self.current_roll

    def set_dice(self, sides: int):
        """Sets Dice-Type"""
        try:
            self.dice_type = DiceType(sides)
            self.sides = self.dice_type.value
        except KeyError:
            print(f"Invalid number of sides. Available options are: {', '.join([die.name for die in DiceType])}")