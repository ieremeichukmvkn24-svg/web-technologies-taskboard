import unittest
from main import count_by_status, total_hours, task_names, tasks

class Practice3Tests(unittest.TestCase):
    def test_count(self):
        self.assertEqual(count_by_status(tasks), {'done': 2, 'doing': 1, 'todo': 1})

    def test_hours(self):
        self.assertEqual(total_hours(tasks), 10)

    def test_done(self):
        self.assertEqual(task_names(tasks, 'done'), ['HTML', 'Git'])

    def test_empty(self):
        self.assertEqual(count_by_status({}), {})
        self.assertEqual(total_hours({}), 0)

if __name__ == '__main__':
    unittest.main()
