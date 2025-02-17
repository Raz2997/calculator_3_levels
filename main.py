import sys
from calculator.calculator import Calculator

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <num1> <num2> <operation>")
        sys.exit(1)

    num1, num2, operation = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        num1, num2 = float(num1), float(num2)
        if operation == "add":
            result = Calculator.add(num1, num2)
        elif operation == "subtract":
            result = Calculator.subtract(num1, num2)
        elif operation == "multiply":
            result = Calculator.multiply(num1, num2)
        elif operation == "divide":
            result = Calculator.divide(num1, num2)
        else:
            print(f"Unknown operation: {operation}")
            sys.exit(1)
        
        print(f"The result of {num1} {operation} {num2} is equal to {result}")

    except ValueError:
        print(f"Invalid number input: {num1} or {num2} is not a valid number.")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero.")

if __name__ == "__main__":
    main()
