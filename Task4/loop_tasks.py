# Print a separator line
print("=" * 50)
print("1️⃣ For Loop: Print numbers from 1 to 100")
print("=" * 50)

# Using for loop to print numbers from 1 to 100
for num in range(1, 101):
    print(num, end=" ")   # end=" " keeps output on the same line

# Move to next section with spacing
print("\n\n" + "=" * 50)
print("2️⃣ While Loop: Countdown Timer")
print("=" * 50)

# Initialize countdown value
countdown = 10

# While loop runs until countdown becomes 0
while countdown > 0:
    print("Countdown:", countdown)
    countdown -= 1        # Decrease countdown by 1 each iteration

print("🚀 Time's up!\n")  # Message after loop ends

# -----------------------------------------------
# Break and Continue Example
# -----------------------------------------------
print("=" * 50)
print("3️⃣ Break and Continue Example")
print("=" * 50)

# Loop from 1 to 10
for num in range(1, 11):

    # Skip number 5 using continue
    if num == 5:
        print("Skipping 5 using continue")
        continue

    # Stop loop completely when number reaches 8
    if num == 8:
        print("Stopping loop at 8 using break")
        break

    print(num)

# -----------------------------------------------
# Iterating Over String Characters
# -----------------------------------------------
print("\n" + "=" * 50)
print("4️⃣ Iterate Over String Characters")
print("=" * 50)

name = "Swathi"

# Loop through each character in the string
for char in name:
    print(char)

# -----------------------------------------------
# Multiplication Table
# -----------------------------------------------
print("\n" + "=" * 50)
print("5️⃣ Multiplication Table")
print("=" * 50)

# Take user input for multiplication table
number = int(input("Enter a number for multiplication table: "))

# Generate multiplication table from 1 to 10
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# -----------------------------------------------
# Range with Steps
# -----------------------------------------------
print("\n" + "=" * 50)
print("6️⃣ Range with Steps")
print("=" * 50)

# Print even numbers using step value 2
print("Even numbers from 2 to 20:")
for num in range(2, 21, 2):
    print(num, end=" ")

# Print odd numbers using step value 2
print("\n\nOdd numbers from 1 to 19:")
for num in range(1, 20, 2):
    print(num, end=" ")

# -----------------------------------------------
# Loop with Conditions (Even / Odd)
# -----------------------------------------------
print("\n\n" + "=" * 50)
print("7️⃣ Loop with Conditions")
print("=" * 50)

# Check whether numbers are even or odd
for num in range(1, 21):
    if num % 2 == 0:
        print(f"{num} → Even Number")
    else:
        print(f"{num} → Odd Number")

# -----------------------------------------------
# Real-World Examples
# -----------------------------------------------
print("\n" + "=" * 50)
print("8️⃣ Real-World Examples Using Loops")
print("=" * 50)

# Example 1: Attendance System
students = ["Rahul", "Anjali", "Swathi", "Kiran"]

print("\n📚 Student Attendance:")
for student in students:
    print(f"Present: {student}")

# Example 2: Shopping Cart Total
prices = [120, 340, 560, 200]
total = 0

# Add all prices to calculate total bill
for price in prices:
    total += price

print("\n🛒 Total Shopping Bill:", total)

# Example 3: Password Attempts System
correct_password = "swathi123"

# Allow user only 3 attempts
for attempt in range(3):
    password = input("\nEnter password: ")

    if password == correct_password:
        print("✅ Access Granted")
        break
    else:
        print("❌ Wrong Password")

# Executes only if loop completes without break
else:
    print("🔒 Account Locked after 3 attempts")

# -----------------------------------------------
# Completion Message
# -----------------------------------------------
print("\n" + "=" * 50)
print("✅ All Loop Tasks Completed Successfully")
print("=" * 50)
