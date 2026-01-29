"""
error_handling.py

This program demonstrates:
1. Using try-except blocks
2. Handling multiple exceptions
3. Using else and finally
4. Logging errors using logging module
5. Saving logs to a file
6. Creating custom error messages
7. Simulating runtime errors
8. Debugging using logs
"""

import logging

# ----------------------------------
# 1. Configure logging
# ----------------------------------

# Create and configure log file
logging.basicConfig(
    filename="app_errors.log",          # Log file name
    level=logging.ERROR,                 # Log only ERROR and above
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("Logging configured. Errors will be saved to app_errors.log")
print("-" * 60)

# ----------------------------------
# 2. Function to demonstrate error handling
# ----------------------------------

def divide_numbers(a, b):
    """
    Divides two numbers and handles possible runtime errors.

    Parameters:
    a (int/float): Numerator
    b (int/float): Denominator
    """
    try:
        result = a / b
    except ZeroDivisionError:
        logging.error("Division by zero attempted.")
        print("Error: Cannot divide by zero.")
    except TypeError:
        logging.error("Invalid data type used for division.")
        print("Error: Please enter numeric values only.")
    else:
        print("Division Result:", result)
    finally:
        print("Division operation completed.\n")


# ----------------------------------
# 3. Function to simulate file error
# ----------------------------------

def read_file(filename):
    """
    Reads a file and handles file-related exceptions.
    """
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        print("Error: File does not exist.")
    except PermissionError:
        logging.error(f"Permission denied for file: {filename}")
        print("Error: Permission denied.")
    else:
        print("File read successfully.")
    finally:
        print("File operation completed.\n")


# ----------------------------------
# 4. Custom validation with custom error message
# ----------------------------------

def check_age(age):
    """
    Validates age input.
    """
    try:
        if age < 0:
            raise ValueError("Age cannot be negative.")
        print("Valid age entered:", age)
    except ValueError as e:
        logging.error(f"Invalid age input: {e}")
        print("Custom Error:", e)
    finally:
        print("Age validation completed.\n")


# ----------------------------------
# 5. Simulating runtime errors
# ----------------------------------

def simulate_runtime_errors():
    """
    Simulates common runtime errors for demonstration.
    """
    try:
        numbers = [1, 2, 3]
        print(numbers[5])   # IndexError
    except IndexError:
        logging.error("Index out of range error occurred.")
        print("Error: List index out of range.")
    finally:
        print("Runtime error simulation completed.\n")


# ----------------------------------
# 6. Main Execution
# ----------------------------------

if __name__ == "__main__":

    print("---- Division Examples ----")
    divide_numbers(10, 2)     # Valid
    divide_numbers(10, 0)     # ZeroDivisionError
    divide_numbers(10, "a")   # TypeError

    print("---- File Handling Example ----")
    read_file("missing_file.txt")   # FileNotFoundError

    print("---- Custom Error Example ----")
    check_age(-5)    # Custom ValueError
    check_age(25)    # Valid case

    print("---- Runtime Error Example ----")
    simulate_runtime_errors()

    print("Program execution completed.")
    print("Check 'app_errors.log' for detailed error logs.")
