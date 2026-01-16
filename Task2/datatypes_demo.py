# datatypes_demo.py
# Demonstrates variables, data types, type conversion, and error handling

# Declaring variables of different data types
integer_var = 10
float_var = 25.5
string_var = "Python"
boolean_var = True

# Printing values and their types
print("Integer:", integer_var, "| Type:", type(integer_var))
print("Float:", float_var, "| Type:", type(float_var))
print("String:", string_var, "| Type:", type(string_var))
print("Boolean:", boolean_var, "| Type:", type(boolean_var))

# Arithmetic operations
print("\nArithmetic Operations:")
print("Addition:", integer_var + float_var)
print("Multiplication:", integer_var * 2)

# Type conversion with error handling
try:
    user_input = input("\nEnter a number: ")
    converted_int = int(user_input)
    converted_float = float(user_input)

    print("Converted to int:", converted_int)
    print("Converted to float:", converted_float)

except ValueError:
    print("Invalid input! Please enter a valid number.")

# String concatenation
age = 21
print("\nMy age is " + str(age))

# Dynamic typing demonstration
value = 100
print("Value:", value, "| Type:", type(value))

value = "Now I am a string"
print("Value:", value, "| Type:", type(value))