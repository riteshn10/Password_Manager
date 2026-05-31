import secrets
import string

# Store generated passwords during the program session
password_history = []


def generate_password():
    print("\n=== Password Generator ===")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be greater than 0.")
            return None
    except ValueError:
        print("Please enter a valid number.")
        return None

    custom_choice = input("Use custom character set? (y/n): ").lower()

    if custom_choice == "y":
        characters = input("Enter custom characters: ")

        if not characters:
            print("Custom character set cannot be empty.")
            return None

    else:
        use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
        use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
        use_numbers = input("Include numbers? (y/n): ").lower() == "y"
        use_symbols = input("Include symbols? (y/n): ").lower() == "y"

        characters = ""

        if use_upper:
            characters += string.ascii_uppercase

        if use_lower:
            characters += string.ascii_lowercase

        if use_numbers:
            characters += string.digits

        if use_symbols:
            characters += string.punctuation

        if not characters:
            print("Error: Select at least one character type.")
            return None

    password = "".join(secrets.choice(characters) for _ in range(length))

    password_history.append(password)

    print("\nGenerated Password:")
    print(password)

    return password


def check_password_strength():
    print("\n=== Password Strength Checker ===")

    password = input("Enter password to check: ")

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase length to at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print(f"\nStrength: {strength}")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")


def view_password_history():
    print("\n=== Password History ===")

    if not password_history:
        print("No passwords generated yet.")
        return

    for index, password in enumerate(password_history, start=1):
        print(f"{index}. {password}")


def save_passwords_to_file():
    print("\n=== Save Passwords ===")

    if not password_history:
        print("No passwords available to save.")
        return

    try:
        with open("passwords.txt", "a") as file:
            file.write("\n===== Saved Passwords =====\n")

            for password in password_history:
                file.write(password + "\n")

        print("Passwords saved successfully to passwords.txt")

    except Exception as error:
        print("Error saving file:", error)


def main():
    while True:
        print("\n" + "=" * 35)
        print("      PASSWORD MANAGER")
        print("=" * 35)
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. View Password History")
        print("4. Save Passwords to File")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            generate_password()

        elif choice == "2":
            check_password_strength()

        elif choice == "3":
            view_password_history()

        elif choice == "4":
            save_passwords_to_file()

        elif choice == "5":
            print("\nThank you for using Password Manager!")
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()