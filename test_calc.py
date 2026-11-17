import unittest

from calc import add, divide, mod, multiply, subtract


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

    def test_mod(self):
        self.assertEqual(mod(7, 3), 1)
        self.assertEqual(mod(6, 3), 0)
        self.assertEqual(mod(-7, 3), 2)
        self.assertEqual(mod(7, -3), -2)

    def test_mod_by_zero(self):
        with self.assertRaises(ValueError):
            mod(1, 0)


if __name__ == "__main__":
    unittest.main()
