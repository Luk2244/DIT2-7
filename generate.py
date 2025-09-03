import unittest
from generator import generate_numbers, generate_target
from checker import check_answer

class TestMathCatch(unittest.TestCase):
    def test_generate_numbers(self):
        nums = generate_numbers()
        self.assertEqual(len(nums), 5)

    def test_generate_target(self):
        target = generate_target()
        self.assertTrue(10 <= target <= 50)

    def test_check_answer_valid(self):
        result, valid = check_answer("2+3", [2, 3], 5)
        self.assertTrue(valid)

    def test_check_answer_invalid(self):
        result, valid = check_answer("9+9", [2, 3], 18)
        self.assertFalse(valid)

if __name__ == "__main__":
    unittest.main()