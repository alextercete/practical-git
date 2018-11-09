import unittest
from calculator import Calculator

class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        calculator = Calculator()
        self.assertEqual(3, calculator.add(1, 2))

    def test_subtraction(self):
        calculator = Calculator()
        self.assertEqual(3, calculator.subtract(5, 2))

    def test_multiplication(self):
        calculator = Calculator()
        self.assertEqual(6, calculator.multiply(3, 2))

if __name__ == '__main__':
    unittest.main()
