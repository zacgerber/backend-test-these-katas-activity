import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(8, 3), 11)
        self.assertEqual(katas.add(-1, 1), 0)
        self.assertEqual(katas.add(-1, -1), -2)

    def test_multiply(self):
        self.assertEqual(katas.multiply(8, 3), 24)
        self.assertEqual(katas.multiply(-1, 1), -1)
        self.assertEqual(katas.multiply(-1, -1), 1)

    def test_power(self):
        self.assertEqual(katas.power(5, 2), 25)
        self.assertEqual(katas.power(-1, 1), -1)
        self.assertEqual(katas.power(-1, -1), 1)

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)
        self.assertEqual(katas.factorial(-1), 1)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(5), 3)
        self.assertEqual(katas.fibonacci(8), 13)


if __name__ == '__main__':
    unittest.main()