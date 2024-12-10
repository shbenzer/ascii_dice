import random

from .ascii_images import ascii_sides
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
    def __init__(self, show_images: bool = True):
        self.dice_type = None
        self.sides = None
        self.rolls = []
        self.current_roll = None
        self.ascii = None
        self.show_images = show_images

    def roll(self) -> int:
        """Rolls the Die"""
        self.current_roll = random.randint(1, self.dice_type.value)
        self.rolls.append(self.current_roll)
        self.ascii = ascii_sides[self.dice_type.value][self.current_roll]
        if self.show_images:
            print(self.ascii)
        return self.current_roll

    def set_dice(self, sides: int):
        """Sets Dice-Type"""
        try:
            self.dice_type = DiceType(sides)
            self.sides = self.dice_type.value
        except KeyError:
            print(f"Invalid number of sides. Available options are: {', '.join([die.name for die in DiceType])}")

    def set_show_images(self, show: bool):
        """Sets whether to show images or not"""
        self.show_images = show

def calculate(rolls: int, die: int, modifier: int, advantage: int = None, show_images: bool = True ) -> int:
    """Performs a simple DnD Calculation with optional Advantage/Disadvantage and Modifiers"""
    if advantage not in [None, -1,1]:
        raise ValueError("Advantage must be -1 (Disadvantage) or 1 (Advantage)")

    if show_images:
        dice = Dice(show_images=True)
    else:
        dice = Dice(show_images=False)

    dice.set_dice(die)

    total = 0

    if advantage == 1:
        for _ in range(rolls):
            roll1 = dice.roll()
            roll2 = dice.roll()
            result = max(roll1, roll2)
            total += result
    elif advantage == -1:
        for _ in range(rolls):
            roll1 = dice.roll()
            roll2 = dice.roll()
            result = min(roll1, roll2)
            total += result
    else:
        for _ in range(rolls):
            result = dice.roll()
            total += result
    return total + modifier