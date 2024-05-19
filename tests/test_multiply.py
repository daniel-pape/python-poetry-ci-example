import unittest
from math_utils.multiply import multiply


class TestApp(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)

if __name__ == "__main__":
    unittest.main()
