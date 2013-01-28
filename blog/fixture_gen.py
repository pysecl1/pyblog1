__author__ = 'User'

import unittest
from fixture_generator import fixture_gen

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
