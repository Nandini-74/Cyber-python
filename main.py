"""
Cyber Security Toolkit (CLI Application)

A menu-driven Python application that integrates multiple
cybersecurity tools into one interface.

Modules:
- Port Scanner
- Brute Force Simulator
- Input Validation Tool
"""

import port_scanner
import brute_force
import validation


def show_menu():
    print("\n=== CYBER SECURITY TOOLKIT ===")
    print("1. Port Scanner")
    print("2. Brute Force Login")
    print("3. Validation Tool")
    print("4. Exit")


# main loop
while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        port_scanner.scan_ports()

    elif choice == "2":
        brute_force.brute_force_login()

    elif choice == "3":
        validation.validate_input()

    elif choice == "4":
        print("Exiting toolkit...")
        break

    else:
        print("Invalid choice. Try again.")
