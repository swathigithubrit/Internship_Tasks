"""
student_records.py

This program demonstrates:
- Using dictionaries to store student records
- Accessing keys and values
- Updating and deleting dictionary entries
- Looping through dictionary data
- Converting dictionary to JSON
- Saving JSON data to a file
- Reading JSON back into Python
- Printing clean formatted output
"""

import json   # Importing JSON module for conversion and file handling


# -----------------------------
# 1. Store student details using dictionary
# -----------------------------

# Dictionary to store student records
students = {
    101: {
        "name": "Swathi",
        "branch": "CSE",
        "year": 4,
        "cgpa": 8.7
    },
    102: {
        "name": "Anil",
        "branch": "ECE",
        "year": 3,
        "cgpa": 8.2
    },
    103: {
        "name": "Priya",
        "branch": "IT",
        "year": 2,
        "cgpa": 8.9
    }
}

print("Initial Student Records:")
print(students)
print("-" * 50)


# -----------------------------
# 2. Access dictionary keys and values
# -----------------------------

print("Student IDs (Keys):")
print(students.keys())

print("\nStudent Details (Values):")
print(students.values())
print("-" * 50)


# -----------------------------
# 3. Update dictionary entries
# -----------------------------

# Updating CGPA of a student
students[102]["cgpa"] = 8.5

# Adding a new student
students[104] = {
    "name": "Ravi",
    "branch": "MECH",
    "year": 1,
    "cgpa": 7.8
}

print("After Updating and Adding Student:")
print(students)
print("-" * 50)


# -----------------------------
# 4. Delete dictionary entry
# -----------------------------

# Deleting a student record
del students[103]

print("After Deleting Student with ID 103:")
print(students)
print("-" * 50)


# -----------------------------
# 5. Loop through dictionary
# -----------------------------

print("Iterating Through Student Records:")
for student_id, details in students.items():
    print(f"\nStudent ID : {student_id}")
    print(f"Name       : {details['name']}")
    print(f"Branch     : {details['branch']}")
    print(f"Year       : {details['year']}")
    print(f"CGPA       : {details['cgpa']}")
print("-" * 50)


# -----------------------------
# 6. Convert dictionary to JSON
# -----------------------------

students_json = json.dumps(students, indent=4)
print("Dictionary Converted to JSON Format:")
print(students_json)
print("-" * 50)


# -----------------------------
# 7. Save JSON to file
# -----------------------------

file_name = "students_data.json"

with open(file_name, "w") as file:
    json.dump(students, file, indent=4)

print(f"Student data successfully saved to {file_name}")
print("-" * 50)


# -----------------------------
# 8. Read JSON back into Python
# -----------------------------

with open(file_name, "r") as file:
    loaded_students = json.load(file)

print("Student Data Read from JSON File:")
print(loaded_students)
print("-" * 50)


# -----------------------------
# 9. Clean formatted output
# -----------------------------

print("Formatted Student Report")
print("=" * 50)

for student_id, details in loaded_students.items():
    print(f"ID     : {student_id}")
    print(f"Name   : {details['name']}")
    print(f"Branch : {details['branch']}")
    print(f"Year   : {details['year']}")
    print(f"CGPA   : {details['cgpa']}")
    print("-" * 50)
