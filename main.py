import os
import json

PASSWORDS_FILE = "Passwords.json"

def init_password_manager():
    
    #check if the file exist
    if os.path.exists(PASSWORDS_FILE):
        print("The file exist.")
    else:
        print ("No such file, creating a new one!")
         #initate the dictinary
        passwords = {}
        #write the diconary to the file
        with open("Passwords.json", "w", encoding="utf-8") as f:
            json.dump(passwords, f, indent=2, ensure_ascii=False)



   

def add_password():
    # Load existing passwords from the file
    with open(PASSWORDS_FILE, "r", encoding="utf-8") as f:
        passwords = json.load(f)

    # Ask user for site and password
    site = input("Enter site name: ").strip()
    password = input("Enter password: ").strip()

    # Check if the site already exists in the vault
    if site in passwords:
        # Ask for confirmation before overwriting
        confirm = input(f"A password already exists for '{site}'. Overwrite? (y/n): ").strip().lower()
        if confirm != "y":
            print("Password not updated.")
            return

    # Add or update the password in the dictionary
    passwords[site] = password

    # Save the updated dictionary back to the file
    with open(PASSWORDS_FILE, "w", encoding="utf-8") as f:
        json.dump(passwords, f, indent=2, ensure_ascii=False)

    # Let the user know it was saved
    print(f"Password for '{site}' saved successfully.")


def remove_password():
    # Load existing passwords from the file
    with open(PASSWORDS_FILE, "r", encoding="utf-8") as f:
        passwords = json.load(f)

    # Ask the user which site to remove
    site = input("What would you like to remove? ").strip()

    # Check if the site exists in the dictionary
    if site in passwords:
        # Ask for confirmation before deleting
        makeSure = input(f"Are you sure you want to delete the password for '{site}'? (y/n)? ").strip().lower()
        if makeSure == "y":
            # Delete the entry and update the file
            del passwords[site]
            with open(PASSWORDS_FILE, "w", encoding="utf-8") as f:
                json.dump(passwords, f, indent=2, ensure_ascii=False)
            print(f"Password for '{site}' deleted.")
        else:
            print("Deletion cancelled.")
    else:
        # Site not found in the vault
        print(f"No password found for '{site}'.")


def get_password():
    # Load the current passwords from the JSON file
    with open(PASSWORDS_FILE, "r", encoding="utf-8") as f:
        passwords = json.load(f)

    # Ask the user which site's password they want to retrieve
    site = input("Please enter the site name to retrieve a password: ").strip()

    # Check if the site exists in the dictionary
    if site in passwords:
        # If it exists, print the password
        print(f"Password for '{site}': {passwords[site]}")
    else:
        # If not, inform the user
        print(f"No password found for '{site}'.")


def main():
    print("Welcome to your personal password manager 🔐")

    # Ensure the JSON file exists before any operations
    init_password_manager()

    while True:
        print("\nPlease choose an option:")
        print("1. Add a password")
        print("2. Get a password")
        print("3. Remove a password")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            remove_password()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please enter a number between 1 and 4.")

# All your function definitions above...

if __name__ == "__main__":
    main()
    