import math


# Create a class called "Calculator" that contains the following.
class Calculator:
    def __init__(self):
        # Initialize the calculator with basic mathematical operations and functions
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
        }

    def add_operation(self, symbol, function):
        # Add a new operation and its corresponding function to the dictionary
        self.operations[symbol] = function

    def calculate(self, num1, symbol, num2):
        # Check if the operation symbol is valid
        if symbol not in self.operations:
            print("Error: Invalid operation symbol.")
            raise ValueError("Invalid operation symbol")

        # Check if the input values are numbers
        if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
            print("Error: Input values must be numbers.")
            raise ValueError("Input values must be numbers")

        # Perform the calculation using the dictionary's function
        operation_function = self.operations[symbol]
        result = operation_function(num1, num2)
        return result

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            raise ZeroDivisionError("Division by zero")
        return num1 / num2

    def exponentiate(self, num1, num2):
        return num1 ** num2

    def square_root(self, num, multiplier):
        return multiplier*math.sqrt(num)

    def logarithm(self, num, base):
        return math.log(num, base)

# Create an instance of the Calculator class
calculator = Calculator()

# Add advanced mathematical operations to the calculator
calculator.add_operation('^', calculator.exponentiate)
calculator.add_operation('sqrt', calculator.square_root)
calculator.add_operation('log', calculator.logarithm)

# Main program
while True:
    try:
        num1 = float(input("Enter the first number: "))
        symbol = input("Enter the operation symbol (+, -, *, /, ^, sqrt, log): ")
        num2 = float(input("When using the square_root function, the second number "
                           "that you give is to multiply the square_root with it.\n"
                           "For instance, if you want the square_root of"
                           " 3, you enter 3 for the first number and 1 for the second one.\n"
                           "And if you want to multiply the square_root of 3 with 2,"
                           "you enter 2 for the second number.\nEnter the second number: "))

        result = calculator.calculate(num1, symbol, num2)
        print('Result', result)
    except ValueError:
        print("Please enter valid input.")
    except ZeroDivisionError:
        pass

    continue_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if continue_calculation != 'yes':
        break
