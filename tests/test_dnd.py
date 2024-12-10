import unittest

from ascii_dice import ascii_sides, Dice, calculate

class TestDnd(unittest.TestCase):
    def test_calculate_single_roll_without_advantage(self):
        """Test a single roll without advantage or modifier"""
        result = calculate(1,20,0,show_images = True)
        self.assertIn(result, range(1,21))

    def test_calculate_single_roll_with_advantage(self):
        """Test a single roll with advantage and no modifier"""
        result = calculate(1,20,0,1,show_images = True)
        self.assertIn(result, range(1,21))

    def test_calculate_single_roll_with_disadvantage(self):
        """Test a single roll with disadvantage and no modifier"""
        result = calculate(1,20,0,-1,show_images = True)
        self.assertIn(result, range(1,21))

    def test_calculate_single_roll_with_advantage_and_modifier(self):
        """Test a single roll with advantage and modifier"""
        modifier = 5
        result = calculate(1,20,modifier,1,show_images = True)
        self.assertIn(result, range(1+modifier,21+modifier))

    def test_calculate_multiple_roll_without_advantage(self):
        """Test a multiple roll without advantage or modifier"""
        rolls = 5
        result = calculate(rolls,20,0,show_images = True)
        self.assertIn(result, range(rolls, 20 * rolls + 1))

    def test_calculate_multiple_roll_with_advantage(self):
        """Test a multiple roll with advantage and no modifier"""
        rolls = 5
        result = calculate(rolls,20,0,1,show_images = True)
        self.assertIn(result, range(rolls, 20 * rolls + 1))

    def test_calculate_multiple_roll_with_disadvantage(self):
        """Test a multiple roll with disadvantage and no modifier"""
        rolls = 5
        result = calculate(rolls,20,0,-1,show_images = True)
        self.assertIn(result, range(rolls, 20 * rolls + 1))

    def test_calculate_multiple_roll_with_advantage_and_modifier(self):
        """Test a multiple roll with advantage and modifier"""
        modifier = 5
        rolls = 5
        result = calculate(rolls,20,modifier,1,show_images = True)
        self.assertIn(result, range(rolls + modifier,20 * rolls + modifier + 1))

if __name__ == "__main__":
    unittest.main()