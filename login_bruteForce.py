"""
Brute Force Login Simulator

This module simulates a brute-force attack on a login system.

It:
- Takes username input
- Tries multiple passwords from a wordlist
- Stops when correct password is found
- Locks after too many attempts

⚠️ Educational purpose only
"""

import time  # used to simulate delay


def brute_force_login():
    """
    This function performs a brute-force attack simulation.
    """

    # -------------------------------
    # Step 1: Setup correct credentials
    # -------------------------------
    
    correct_username = "admin"
    correct_password = "secure@123"

    # -------------------------------
    # Step 2: Take user input
    # -------------------------------
    
    username = input("Enter username: ")

    # -------------------------------
    # Step 3: Wordlist (password guesses)
    # -------------------------------
    
    wordlist = ["123456", "password", "admin123", "letmein", "secure@123"]

    # -------------------------------
    # Step 4: Initialize counters
    # -------------------------------
    
    attempts = 0
    max_attempts = 5

    print("\nStarting brute force attack...\n")

    # -------------------------------
    # Step 5: Loop through passwords
    # -------------------------------
    
    for password in wordlist:
        time.sleep(0.5)  # simulate real attack delay

        print(f"Trying: {password}")
        attempts += 1

        # -------------------------------
        # Step 6: Check credentials
        # -------------------------------
        
        if username == correct_username and password == correct_password:
            print("\n✅ ACCESS GRANTED")
            print(f"Password found: {password}")
            print(f"Attempts: {attempts}")
            break

        else:
            print("❌ Incorrect")

        # -------------------------------
        # Step 7: Lock mechanism
        # -------------------------------
        
        if attempts >= max_attempts:
            print("\n🔒 Account Locked! Too many attempts.")
            break
