"""
collections_demo.py

This program demonstrates the usage of Python collections:
- List
- Tuple
- Set

It covers:
- Adding, removing, sorting list elements
- Using tuple for fixed data
- Removing duplicates using set
- Set operations
- Iterating over collections
- Mutable vs Immutable comparison
- Formatted output
"""

# -----------------------------
# 1. LIST: Store student names
# -----------------------------

# Creating a list of student names
students = ["Swathi", "Anil", "Ravi", "Anil", "Priya"]

print("Initial Student List:")
print(students)
print("-" * 40)

# -----------------------------
# 2. Add elements to the list
# -----------------------------

students.append("Kiran")   # Adds element at the end
print("After Adding a Student:")
print(students)
print("-" * 40)

# -----------------------------
# 3. Remove elements from list
# -----------------------------

students.remove("Ravi")    # Removes specified element
print("After Removing a Student:")
print(students)
print("-" * 40)

# -----------------------------
# 4. Sort the list
# -----------------------------

students.sort()            # Sorts list alphabetically
print("After Sorting the Student List:")
print(students)
print("-" * 40)

# -----------------------------
# 5. TUPLE: Fixed data
# -----------------------------

# Tuple for fixed data (immutable)
course_info = ("Python Programming", 6, "Online")

print("Course Information (Tuple):")
print(f"Course Name : {course_info[0]}")
print(f"Duration    : {course_info[1]} weeks")
print(f"Mode        : {course_info[2]}")
print("-" * 40)

# -----------------------------
# 6. Convert list to set (remove duplicates)
# -----------------------------

student_set = set(students)  # Removes duplicates automatically

print("Unique Student Names (Set):")
print(student_set)
print("-" * 40)

# -----------------------------
# 7. Perform set operations
# -----------------------------

new_students = {"Akhil", "Priya", "Swathi"}

print("Another Set of Students:")
print(new_students)
print("-" * 40)

# Union
print("Union of Sets:")
print(student_set.union(new_students))

# Intersection
print("\nIntersection of Sets:")
print(student_set.intersection(new_students))

# Difference
print("\nDifference of Sets:")
print(student_set.difference(new_students))
print("-" * 40)

# -----------------------------
# 8. Iterating over collections
# -----------------------------

print("Iterating over Student List:")
for student in students:
    print(f"- {student}")

print("\nIterating over Student Set:")
for student in student_set:
    print(f"- {student}")

print("\nIterating over Course Tuple:")
for item in course_info:
    print(f"- {item}")

print("-" * 40)

# -----------------------------
# 9. Mutable vs Immutable
# -----------------------------

print("Mutable vs Immutable Comparison:")

# List is mutable
students[0] = "Sita"
print("Modified List (Mutable):")
print(students)

# Tuple is immutable
print("\nTrying to modify tuple will cause error:")
print("course_info[0] = 'Java'  # ❌ Not allowed")

print("-" * 40)

# -----------------------------
# 10. Formatted Output Summary
# -----------------------------

print("Formatted Summary Output:")
print(f"Total Students (List) : {len(students)}")
print(f"Unique Students (Set) : {len(student_set)}")
print(f"Course Name           : {course_info[0]}")
