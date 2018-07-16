class Calculator:
    def add(self, firstNumber, secondNumber):
        return firstNumber + secondNumber

    def subtract(self, firstNumber, secondNumber):
        return firstNumber - secondNumber

    def multiply(self, firstNumber, secondNumber):
        return firstNumber * secondNumber

    def divide(self, firstNumber, secondNumber):
        if secondNumber == 0:
            raise ValueError('Cannot divide by zero!')
        return firstNumber / secondNumber
