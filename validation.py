"""
Input Validation Tool

This module validates user inputs such as email and password.

It:
- Checks email format
- Checks password strength

⚠️ Educational purpose only
"""

import re  # used for pattern matching


def validate_input():
    """
    This function validates email and password input.
    """

    # -------------------------------
    # Step 1: Take user input
    # -------------------------------
    
    email = input("Enter email: ")
    password = input("Enter password: ")

    # -------------------------------
    # Step 2: Validate Email
    # -------------------------------
    
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if re.match(email_pattern, email):
        print("✅ Valid Email")
    else:
        print("❌ Invalid Email")

    # -------------------------------
    # Step 3: Validate Password
    # -------------------------------
    
    if len(password) < 8:
        print("❌ Password too short")
    
    elif not any(char.isupper() for char in password):
        print("❌ Must include uppercase letter")
    
    elif not any(char.islower() for char in password):
        print("❌ Must include lowercase letter")
    
    elif not any(char.isdigit() for char in password):
        print("❌ Must include a number")
    
    else:
        print("✅ Strong Password")
