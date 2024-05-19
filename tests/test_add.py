import unittest
from math_utils.add import add


class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-1, 0), -1)
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-2, 0), -2)
        self.assertEqual(add(-2, -2), -4)


if __name__ == "__main__":
    unittest.main()
