import unittest

from ascii_dice import ascii_sides, Dice, DiceType

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
    
    def test_calculate_single_roll_without_advantage(self):
        """Test a single roll without advantage or modifier"""
        result = Dice.calculate(1,20,0,show_images = True)
        self.assertIn(result, range(1,21))

    def test_calculate_single_roll_with_advantage(self):
        """Test a single roll with advantage and no modifier"""
        result = Dice.calculate(1,20,0,1,show_images = True)
        self.assertIn(result, range(1,21))

    def test_calculate_single_roll_with_disadvantage(self):
        """Test a single roll with disadvantage and no modifier"""
        result = Dice.calculate(1,20,0,-1,show_images = True)
        self.assertIn(result, range(1,21))

    def test_calculate_single_roll_with_advantage_and_modifier(self):
        """Test a single roll with advantage and modifier"""
        modifier = 5
        result = Dice.calculate(1,20,modifier,1,show_images = True)
        self.assertIn(result, range(1+modifier,21+modifier))

    def test_calculate_multiple_roll_without_advantage(self):
        """Test a multiple roll without advantage or modifier"""
        rolls = 5
        result = Dice.calculate(rolls,20,0,show_images = True)
        self.assertIn(result, range(rolls, 20 * rolls + 1))

    def test_calculate_multiple_roll_with_advantage(self):
        """Test a multiple roll with advantage and no modifier"""
        rolls = 5
        result = Dice.calculate(rolls,20,0,1,show_images = True)
        self.assertIn(result, range(rolls, 20 * rolls + 1))

    def test_calculate_multiple_roll_with_disadvantage(self):
        """Test a multiple roll with disadvantage and no modifier"""
        rolls = 5
        result = Dice.calculate(rolls,20,0,-1,show_images = True)
        self.assertIn(result, range(rolls, 20 * rolls + 1))

    def test_calculate_multiple_roll_with_advantage_and_modifier(self):
        """Test a multiple roll with advantage and modifier"""
        modifier = 5
        rolls = 5
        result = Dice.calculate(rolls,20,modifier,1,show_images = True)
        self.assertIn(result, range(rolls + modifier,20 * rolls + modifier + 1))

if __name__ == "__main__":
    unittest.main()