# hello_world.py
# This program prints user details and demonstrates basic input/output

# Importing datetime module to get today's date
from datetime import date

# Taking user input
name = input("Enter your name: ")
role = input("Enter your internship role: ")

# Getting today's date
today_date = date.today()

# Printing the output
print("\n--- Internship Details ---")
print("Name:", name)
print("Role:", role)
print("Date:", today_date)
