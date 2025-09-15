Password Generator
Description
A Python-based advanced password generator with a graphical user interface (GUI) built using Tkinter. It allows users to create secure, random passwords with customizable length (8-50 characters), character types (lowercase, uppercase, digits, symbols), and excluded characters. The app includes a password strength indicator and clipboard integration for easy copying.
Features

Customizable Passwords: Specify length and select character types (lowercase, uppercase, digits, symbols).
Exclude Characters: Avoid specific characters (e.g., Il1O0) to prevent confusion.
Password Strength Indicator: Classifies passwords as Weak, Moderate, or Strong based on length and character diversity.
Clipboard Integration: Copy generated passwords to the system clipboard with one click.
Input Validation: Ensures valid length and character type selections with clear error messages.
User-Friendly GUI: Intuitive interface built with Tkinter.

Requirements

Python 3.6+
Tkinter (included with standard Python installation)
Pyperclip (pip install pyperclip)

Installation

Clone the repository:git clone  https://github.com/rohit0090/random_password_generator.git


Navigate to the project directory:cd password_generator


Install dependencies:pip install -r requirements.txt



Usage

Run the script:python random_password.py


In the GUI:
Enter a password length (8-50).
Select desired character types (lowercase, uppercase, digits, symbols).
Optionally, enter characters to exclude (e.g., Il1O0).
Click "Generate Password" to create a password.
Click "Copy to Clipboard" to copy the generated password.
View the password strength (Weak, Moderate, or Strong).



Example

Input:
Length: 12
Character Types: All selected
Excluded Characters: Il1O0


Output: A password like Kj#9mP&x2v$Q
Strength: Strong

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major updates, open an issue to discuss first.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Author

Rohit (GitHub: rohit0090)
