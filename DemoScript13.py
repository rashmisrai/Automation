# Static method

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# Example usage
result_add = MathOperations.add(10, 5)
print("Addition:", result_add)
result_subtract = MathOperations.subtract(10, 5)
print("Subtraction:", result_subtract)
result_multiply = MathOperations.multiply(10, 5)
print("Multiplication:", result_multiply)
result_divide = MathOperations.divide(10, 5)
print("Division:", result_divide)

