import unittest
from main import validate_task, get_recommendation

class Practice1Tests(unittest.TestCase):
    def test_validation_success(self):
        self.assertTrue(validate_task("HTML", 60, 2)[0])

    def test_validation_empty_name(self):
        self.assertFalse(validate_task(" ", 60, 2)[0])

    def test_validation_bad_minutes(self):
        self.assertFalse(validate_task("HTML", -1, 2)[0])

    def test_priority_and_urgent(self):
        self.assertIn("зараз", get_recommendation(20, 3, True))

    def test_logical_or(self):
        self.assertIn("сьогодні", get_recommendation(180, 1, False))

if __name__ == '__main__':
    unittest.main()
