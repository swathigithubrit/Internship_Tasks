
# Function to calculate grade
def calculate_grade(marks):
    # Check if marks are valid
    if marks < 0 or marks > 100:
        return "Invalid marks! Please enter a number between 0 and 100."
    
    # Nested and logical conditions to determine grade
    if marks >= 90:
        return "Grade: A+ (Excellent)"
    elif marks >= 80 and marks < 90:
        return "Grade: A (Very Good)"
    elif marks >= 70 and marks < 80:
        return "Grade: B (Good)"
    elif marks >= 60 and marks < 70:
        return "Grade: C (Average)"
    elif marks >= 50 and marks < 60:
        # Nested condition for borderline case
        if marks == 55:
            return "Grade: C+ (Just Passed)"
        else:
            return "Grade: C (Pass)"
    else:
        return "Grade: F (Fail)"

# Main program
def main():
    try:
        # Take input from user
        marks = float(input("Enter your marks (0-100): "))
        # Calculate grade
        grade_message = calculate_grade(marks)
        # Display the result
        print(grade_message)
    except ValueError:
        print("Invalid input! Please enter numeric marks only.")

# Run the program
if __name__ == "__main__":
    main()
