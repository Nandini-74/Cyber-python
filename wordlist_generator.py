"""
Wordlist Generator Tool

This module generates possible passwords based on user input.

It:
- Takes name and birth year
- Creates common password patterns
- Outputs a wordlist

Educational purpose only
"""

def generate_wordlist():
    """
    This function generates a list of possible passwords.
    """

    # -------------------------------
    # Step 1: Take user input
    # -------------------------------
    
    name = input("Enter name: ")
    year = input("Enter birth year: ")

    # -------------------------------
    # Step 2: Generate variations
    # -------------------------------
    
    wordlist = []

    wordlist.append(name)
    wordlist.append(name + "123")
    wordlist.append(name + year)
    wordlist.append(name + "@123")
    wordlist.append(name.capitalize() + "123")
    wordlist.append(name.lower() + year)
    wordlist.append(name + "@" + year)

    # -------------------------------
    # Step 3: Display results
    # -------------------------------
    
    print("\nGenerated Wordlist:\n")

    for word in wordlist:
        print(word)

    print("\nTotal passwords generated:", len(wordlist))