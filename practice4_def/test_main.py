"""Автоматична перевірка практичної 4 через стандартний unittest."""
import unittest

from main import check_name, completion_percent, get_priority_name, task_summary, total_hours


class FunctionTests(unittest.TestCase):
    def test_valid_name(self):
        self.assertTrue(check_name("HTML"))
        self.assertFalse(check_name(" "))

    def test_priority(self):
        self.assertEqual(get_priority_name(3), "високий")
        with self.assertRaises(ValueError):
            get_priority_name(7)

    def test_hours(self):
        self.assertEqual(total_hours([1, 2.5]), 3.5)
        with self.assertRaises(ValueError):
            total_hours([-1])

    def test_progress(self):
        self.assertEqual(completion_percent(3, 4), 75.0)
        self.assertEqual(completion_percent(0, 0), 0.0)
        with self.assertRaises(ValueError):
            completion_percent(5, 2)

    def test_summary(self):
        self.assertIn("виконано", task_summary("Сайт", 2, True))
        with self.assertRaises(ValueError):
            task_summary("", 2)


if __name__ == "__main__":
    unittest.main()
