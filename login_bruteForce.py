"""
Login Brute Force Simulator (Learning Version)

This program simulates a brute-force attack on a login system.

It tries multiple passwords from a wordlist until it finds the correct one.

Features:
- Username input
- Password guessing using list
- Attempt limiting (account lock)
- Delay to simulate real attack
- Time taken to crack password

 Educational purpose only
"""

import time   # used to add delay and track time


def brute_force_login():
    
    # -------------------------------
    # Step 1: Setup correct credentials
    # -------------------------------
    correct_username = "admin"
    correct_password = "secure@123"

    # -------------------------------
    # Step 2: Take username input
    # -------------------------------
    username = input("Enter username: ")

    # -------------------------------
    # Step 3: Create wordlist (password guesses)
    # -------------------------------
    wordlist = ["123456", "password", "admin123", "letmein", "secure@123"]

    # -------------------------------
    # Step 4: Initialize counters
    # -------------------------------
    attempts = 0
    max_attempts = 5

    # -------------------------------
    # Step 5: Start timer
    # -------------------------------
    start_time = time.time()

    print("\nStarting brute force attack...\n")

    # -------------------------------
    # Step 6: Loop through each password
    # -------------------------------
    for password in wordlist:
        
        # simulate delay (real attack feel)
        time.sleep(0.5)

        # show current attempt
        print(f"Trying: {password}")

        # increase attempt count
        attempts += 1

        # -------------------------------
        # Step 7: Check credentials
        # -------------------------------
        if username == correct_username and password == correct_password:
            print("\n ACCESS GRANTED")
            print(f"Password found: {password}")
            print(f"Attempts: {attempts}")
            
            # stop timer
            end_time = time.time()
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            break

        else:
            print("Incorrect")

        # -------------------------------
        # Step 8: Lock account after max attempts
        # -------------------------------
        if attempts >= max_attempts:
            print("\n Account Locked! Too many failed attempts.")
            
            end_time = time.time()
            print(f"Time taken: {end_time - start_time:.2f} seconds")
            break


# -------------------------------
# Step 9: Run the program
# -------------------------------
brute_force_login()