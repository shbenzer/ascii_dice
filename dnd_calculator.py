import random

from ascii_images import ascii_sides

def calculate(rolls: int, die: int, modifier: int, advantage: int = None ) -> int:
    """Performs a simple DnD Calculation with Advantage/Disadvantage"""
    if advantage not in [None, -1,1]:
        raise ValueError("Advantage must be -1 (Disadvantage) or 1 (Advantage)")
    total = 0
    if advantage == 1:
        for _ in range(rolls):
            result = max(random.randint(1, die),random.randint(1, die))
            print(ascii_sides[die][result])
            total += result
    elif advantage == -1:
        for _ in range(rolls):
            result = min(random.randint(1, die),random.randint(1, die))
            print(ascii_sides[die][result])
            total += result
    else:
        for _ in range(rolls):
            result = random.randint(1, die)
            print(ascii_sides[die][result])
            total += result
    return total + modifier