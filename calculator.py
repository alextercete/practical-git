class Calculator:
    def add(self, operand1, operand2):
        return operand1 + operand2

    def subtract(self, operand1, operand2):
        return operand1 - operand2

    def multiply(self, operand1, operand2):
        return operand1 * operand2

    def divide(self, operand1, operand2):
        if operand2 == 0:
            raise ValueError('Cannot divide by zero!')
        return operand1 / operand2
