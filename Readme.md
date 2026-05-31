# Password Manager 🔐

A secure and user-friendly command-line Password Manager built with Python.

## Features

* Generate strong random passwords
* Password Strength Checker
* Password History Tracking
* Custom Character Set Support
* Save Passwords to a File
* Menu-Driven Interface
* Input Validation
* Secure Password Generation using Python's `secrets` module

## Technologies Used

* Python 3
* `secrets`
* `string`

## Project Structure

```text
Password-Manager/
│
├── password_manager.py
├── README.md
├── .gitignore
└── passwords.txt
```

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Navigate to the project folder:

```bash
cd Password-Manager
```

3. Run the program:

```bash
python password_manager.py
```

## Menu Options

```text
1. Generate Password
2. Check Password Strength
3. View Password History
4. Save Passwords to File
5. Exit
```

## Password Strength Criteria

The strength checker evaluates:

* Password length (8+ characters)
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

Ratings:

* Weak
* Medium
* Strong

## Example

```text
=== Password Generator ===

Enter password length: 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

Generated Password:
A@7kLm!29xQ#
```

## Why This Project?

This project demonstrates:

* Python fundamentals
* Functions and modular programming
* File handling
* Input validation
* Secure random generation
* Command-line application design

## Future Improvements

* Password encryption
* Master password authentication
* Password manager database
* Password expiration checker
* GUI version using Tkinter or CustomTkinter

## License

This project is open-source and available under the MIT License.
