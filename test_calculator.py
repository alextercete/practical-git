import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(3, self.calculator.add(1, 2))

    def test_subtraction(self):
        self.assertEqual(3, self.calculator.subtract(5, 2))

    def test_multiplication(self):
        self.assertEqual(6, self.calculator.multiply(3, 2))

    def test_division(self):
        self.assertEqual(6, self.calculator.divide(12, 2))

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(12, 0)

if __name__ == '__main__':
    unittest.main()
