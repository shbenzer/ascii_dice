import unittest

from ascii_dice import ascii_sides, Dice, DiceType, calculate

class TestDice(unittest.TestCase):
    def test_create_die(self):
        """Test construction of Dice"""
        dice = Dice()
        dice.set_dice(6)
        self.assertEqual(dice.dice_type, DiceType.D6)
        self.assertEqual(dice.sides, 6)

    def test_roll_die(self):
        """Test rolling of Dice"""
        dice = Dice()
        dice.set_dice(6)
        dice.roll()
        self.assertIn(dice.current_roll, range(1, 7))

    def test_multiple_rolls(self):
        """Test multiple rolls of Dice"""
        dice = Dice()
        dice.set_dice(6)
        for _ in range(100):
            dice.roll()
        self.assertTrue(all(roll in range(1, 7) for roll in dice.rolls))

    def test_correct_ascii(self):
        """Test correct ascii representation of Dice"""
        dice = Dice()
        dice.set_dice(6)
        dice.roll()
        self.assertIn(str(dice.current_roll), dice.ascii)
        self.assertEqual(dice.ascii, ascii_sides[dice.sides][dice.current_roll])

    def test_change_dice(self):
        """Test changing of Dice"""
        dice = Dice()
        dice.set_dice(6)
        self.assertEqual(dice.dice_type, DiceType.D6)
        dice.set_dice(20)
        self.assertEqual(dice.dice_type, DiceType.D20)

if __name__ == "__main__":
    unittest.main()