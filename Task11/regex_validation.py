# regex_validation.py
# --------------------------------------------------
# This file centralizes all validation logic using
# Regular Expressions (regex).
#
# Validations covered:
# 1. Email validation
# 2. Indian mobile number validation
# 3. Password validation
#
# Concepts demonstrated:
# - re module usage
# - Pattern matching
# - Reusable functions
# - Input validation
# - Edge case handling
# --------------------------------------------------

import re


# --------------------------------------------------
# Email Validation
# --------------------------------------------------
def validate_email(email):
    """
    Validates an email address using regex.

    Rules:
    - Starts with letters/numbers
    - Can contain dots or underscores
    - Must contain '@'
    - Valid domain name
    """

    if not email:
        return "Email cannot be empty"

    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.fullmatch(email_pattern, email):
        return "Valid email address"
    else:
        return "Invalid email format"


# --------------------------------------------------
# Indian Mobile Number Validation
# --------------------------------------------------
def validate_mobile(mobile):
    """
    Validates Indian mobile numbers.

    Rules:
    - Exactly 10 digits
    - Starts with 6, 7, 8, or 9
    """

    if not mobile:
        return "Mobile number cannot be empty"

    mobile_pattern = r'^[6-9]\d{9}$'

    if re.fullmatch(mobile_pattern, mobile):
        return "Valid Indian mobile number"
    else:
        return "Invalid mobile number"


# --------------------------------------------------
# Password Validation
# --------------------------------------------------
def validate_password(password):
    """
    Validates password strength.

    Rules:
    - Minimum 8 characters
    - At least one digit
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one special character
    """

    if not password:
        return "Password cannot be empty"

    password_pattern = (
        r'^(?=.*[a-z])'      # at least one lowercase letter
        r'(?=.*[A-Z])'       # at least one uppercase letter
        r'(?=.*\d)'          # at least one digit
        r'(?=.*[@$!%*?&])'   # at least one special character
        r'[A-Za-z\d@$!%*?&]{8,}$'  # minimum length 8
    )

    if re.fullmatch(password_pattern, password):
        return "Strong password"
    else:
        return "Weak password (does not meet criteria)"


# --------------------------------------------------
# Main Program – User Interaction
# --------------------------------------------------
def main():
    """
    Accepts user input dynamically and performs validation
    """

    print("\n--- REGEX VALIDATION SYSTEM ---\n")

    # Email validation
    email = input("Enter email address: ").strip()
    print(validate_email(email))

    print("-" * 40)

    # Mobile number validation
    mobile = input("Enter Indian mobile number: ").strip()
    print(validate_mobile(mobile))

    print("-" * 40)

    # Password validation
    password = input("Enter password: ").strip()
    print(validate_password(password))


# --------------------------------------------------
# Program Execution Entry Point
# --------------------------------------------------
if __name__ == "__main__":
    main()
