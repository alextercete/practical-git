class Calculator:
    def add(self, operand1, operand2):
        print('Called add')
        return operand1 + operand2

    def subtract(self, operand1, operand2):
        return operand1 - operand2

    def multiply(self, operand1, operand2):
        return operand1 * operand2

    def divide(self, operand1, operand2):
        # TODO: raise ValueError when operand2 is zero
        return operand1 / operand2
