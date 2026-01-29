"""
calculator.py

A simple calculator program that performs basic arithmetic operations:
addition, subtraction, multiplication, and division.

Features:
- Uses functions with parameters and return values
- Uses default arguments
- Handles division by zero
- Separates logic into multiple functions
- Includes docstrings and comments
"""

# -----------------------------
# Arithmetic Operation Functions
# -----------------------------

def add(a=0, b=0):
    """
    Add two numbers.

    Parameters:
    a (float): First number (default is 0)
    b (float): Second number (default is 0)

    Returns:
    float: Sum of a and b
    """
    return a + b


def subtract(a=0, b=0):
    """
    Subtract second number from first number.

    Parameters:
    a (float): First number (default is 0)
    b (float): Second number (default is 0)

    Returns:
    float: Difference of a and b
    """
    return a - b


def multiply(a=1, b=1):
    """
    Multiply two numbers.

    Parameters:
    a (float): First number (default is 1)
    b (float): Second number (default is 1)

    Returns:
    float: Product of a and b
    """
    return a * b


def divide(a=1, b=1):
    """
    Divide first number by second number.

    Parameters:
    a (float): Numerator (default is 1)
    b (float): Denominator (default is 1)

    Returns:
    float: Division result if b is not zero
    str: Error message if division by zero occurs
    """
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


# -----------------------------
# Utility Functions
# -----------------------------

def get_user_input():
    """
    Takes two numbers as input from the user.

    Returns:
    tuple: Two float numbers entered by the user
    """
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2


def display_menu():
    """
    Displays calculator options to the user.
    """
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


# -----------------------------
# Main Logic Function
# -----------------------------

def calculator():
    """
    Main function that runs the calculator.
    """
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        # Exit condition
        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break

        # Validate choice
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please try again.")
            continue

        # Get numbers from user
        num1, num2 = get_user_input()

        # Perform operation based on choice
        if choice == "1":
            result = add(num1, num2)
            print("Result:", result)

        elif choice == "2":
            result = subtract(num1, num2)
            print("Result:", result)

        elif choice == "3":
            result = multiply(num1, num2)
            print("Result:", result)

        elif choice == "4":
            result = divide(num1, num2)
            print("Result:", result)


# -----------------------------
# Test Functions Independently
# -----------------------------

def test_functions():
    """
    Tests all arithmetic functions independently.
    """
    print("\n--- Testing Functions ---")
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))
    print("Divide by zero:", divide(10, 0))


# -----------------------------
# Program Entry Point
# -----------------------------

if __name__ == "__main__":
    # Run tests
    test_functions()

    # Run calculator
    calculator()
