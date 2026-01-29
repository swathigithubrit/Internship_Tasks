"""
file_handling_demo.py

This program demonstrates:
1. Creating a text file using Python
2. Writing user data into a file
3. Reading file contents
4. Appending data to the file
5. Handling file-related exceptions
6. Creating a CSV file using csv module
7. Writing multiple rows to CSV
8. Reading CSV data
9. Closing files properly using 'with' statement
"""

import csv   # Importing csv module

# --------------------------------
# 1. Create a text file & write data
# --------------------------------

try:
    with open("user_data.txt", "w") as file:
        name = input("Enter your name: ")
        age = input("Enter your age: ")

        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")

    print("Data written to user_data.txt successfully.")

except IOError as e:
    print("File write error:", e)

print("-" * 50)

# -----------------------------
# 2. Read file contents
# -----------------------------

try:
    with open("user_data.txt", "r") as file:
        content = file.read()
        print("Reading file contents:")
        print(content)

except FileNotFoundError:
    print("File not found.")
except IOError as e:
    print("File read error:", e)

print("-" * 50)

# -----------------------------
# 3. Append data to file
# -----------------------------

try:
    with open("user_data.txt", "a") as file:
        city = input("Enter your city: ")
        file.write(f"City: {city}\n")

    print("Data appended successfully.")

except IOError as e:
    print("File append error:", e)

print("-" * 50)

# -----------------------------
# 4. Create a CSV file & write data
# -----------------------------

try:
    with open("students.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        # Writing header
        writer.writerow(["ID", "Name", "Branch", "CGPA"])

        # Writing multiple rows
        writer.writerow([101, "Swathi", "CSE", 8.7])
        writer.writerow([102, "Anil", "ECE", 8.3])
        writer.writerow([103, "Priya", "IT", 8.9])

    print("CSV file created and data written successfully.")

except IOError as e:
    print("CSV write error:", e)

print("-" * 50)

# -----------------------------
# 5. Read CSV data
# -----------------------------

try:
    with open("students.csv", "r") as csv_file:
        reader = csv.reader(csv_file)

        print("Reading CSV file:")
        for row in reader:
            print(row)

except FileNotFoundError:
    print("CSV file not found.")
except IOError as e:
    print("CSV read error:", e)

print("-" * 50)

# -----------------------------
# End of Program
# -----------------------------
