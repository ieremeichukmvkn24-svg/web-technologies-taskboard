import unittest
from main import add_task, remove_task, get_tasks

class Practice2Tests(unittest.TestCase):
    def test_add(self):
        tasks = []
        self.assertTrue(add_task(tasks, ' HTML '))
        self.assertEqual(tasks, ['HTML'])

    def test_duplicate(self):
        tasks = ['HTML']
        self.assertFalse(add_task(tasks, 'HTML'))

    def test_remove(self):
        tasks = ['HTML', 'CSS']
        self.assertTrue(remove_task(tasks, 'CSS'))
        self.assertEqual(tasks, ['HTML'])

    def test_remove_missing(self):
        self.assertFalse(remove_task([], 'CSS'))

    def test_list(self):
        self.assertIn('1. HTML', get_tasks(['HTML']))

if __name__ == '__main__':
    unittest.main()
