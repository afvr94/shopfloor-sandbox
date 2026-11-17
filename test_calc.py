import unittest

from calc import add, average, divide, multiply, percent, sqrt, subtract


class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(7, 0), 0)
        self.assertEqual(multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_sqrt(self):
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(0), 0)
        self.assertAlmostEqual(sqrt(2), 1.41421356, places=7)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_percent(self):
        self.assertEqual(percent(50, 200), 25)
        self.assertEqual(percent(0, 10), 0)
        self.assertAlmostEqual(percent(1, 3), 33.3333333, places=6)
        self.assertEqual(percent(-5, 20), -25)

    def test_percent_of_zero(self):
        with self.assertRaises(ValueError):
            percent(1, 0)

    def test_average(self):
        self.assertEqual(average([1, 2, 3]), 2)
        self.assertEqual(average([7]), 7)
        self.assertEqual(average([-4, -2, 0]), -2)
        self.assertAlmostEqual(average([0.1, 0.2, 0.3]), 0.2)
        self.assertEqual(average((2, 4)), 3)
        self.assertEqual(average(x for x in [1, 2, 3, 4]), 2.5)

    def test_average_empty(self):
        with self.assertRaises(ValueError):
            average([])


if __name__ == "__main__":
    unittest.main()
