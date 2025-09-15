import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("400x500")
        
        # Character sets
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = string.punctuation
        
        # GUI Elements
        self.create_gui()
        
    def create_gui(self):
        # Password Length
        tk.Label(self.root, text="Password Length (8-50):").pack(pady=5)
        self.length_entry = tk.Entry(self.root)
        self.length_entry.pack(pady=5)
        self.length_entry.insert(0, "12")
        
        # Character Type Checkboxes
        self.lowercase_var = tk.BooleanVar(value=True)
        self.uppercase_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        
        tk.Checkbutton(self.root, text="Include Lowercase", variable=self.lowercase_var).pack(pady=5)
        tk.Checkbutton(self.root, text="Include Uppercase", variable=self.uppercase_var).pack(pady=5)
        tk.Checkbutton(self.root, text="Include Digits", variable=self.digits_var).pack(pady=5)
        tk.Checkbutton(self.root, text="Include Symbols", variable=self.symbols_var).pack(pady=5)
        
        # Excluded Characters
        tk.Label(self.root, text="Exclude Characters (e.g., Il1O0):").pack(pady=5)
        self.exclude_entry = tk.Entry(self.root)
        self.exclude_entry.pack(pady=5)
        
        # Generate Button
        tk.Button(self.root, text="Generate Password", command=self.generate_password).pack(pady=10)
        
        # Password Display
        self.password_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.password_var, state='readonly', width=30).pack(pady=5)
        
        # Copy to Clipboard Button
        tk.Button(self.root, text="Copy to Clipboard", command=self.copy_to_clipboard).pack(pady=5)
        
        # Password Strength Indicator
        self.strength_var = tk.StringVar(value="Strength: N/A")
        tk.Label(self.root, textvariable=self.strength_var).pack(pady=5)
        
    def validate_inputs(self):
        try:
            length = int(self.length_entry.get())
            if length < 8 or length > 50:
                messagebox.showerror("Error", "Password length must be between 8 and 50.")
                return False
        except ValueError:
            messagebox.showerror("Error", "Password length must be a valid number.")
            return False
            
        if not any([self.lowercase_var.get(), self.uppercase_var.get(), 
                   self.digits_var.get(), self.symbols_var.get()]):
            messagebox.showerror("Error", "At least one character type must be selected.")
            return False
            
        return True
    
    def check_password_strength(self, password):
        score = 0
        if len(password) >= 12:
            score += 1
        if self.lowercase_var.get() and any(c in self.lowercase for c in password):
            score += 1
        if self.uppercase_var.get() and any(c in self.uppercase for c in password):
            score += 1
        if self.digits_var.get() and any(c in self.digits for c in password):
            score += 1
        if self.symbols_var.get() and any(c in self.symbols for c in password):
            score += 1
            
        if score <= 2:
            return "Weak"
        elif score <= 4:
            return "Moderate"
        else:
            return "Strong"
    
    def generate_password(self):
        if not self.validate_inputs():
            return
            
        length = int(self.length_entry.get())
        exclude_chars = set(self.exclude_entry.get())
        
        # Build character pool
        char_pool = ""
        if self.lowercase_var.get():
            char_pool += self.lowercase
        if self.uppercase_var.get():
            char_pool += self.uppercase
        if self.digits_var.get():
            char_pool += self.digits
        if self.symbols_var.get():
            char_pool += self.symbols
            
        # Remove excluded characters
        char_pool = ''.join(c for c in char_pool if c not in exclude_chars)
        
        if not char_pool:
            messagebox.showerror("Error", "No characters available after exclusions.")
            return
            
        # Ensure at least one character from each selected type
        password = []
        if self.lowercase_var.get():
            password.append(random.choice([c for c in self.lowercase if c not in exclude_chars]))
        if self.uppercase_var.get():
            password.append(random.choice([c for c in self.uppercase if c not in exclude_chars]))
        if self.digits_var.get():
            password.append(random.choice([c for c in self.digits if c not in exclude_chars]))
        if self.symbols_var.get():
            password.append(random.choice([c for c in self.symbols if c not in exclude_chars]))
            
        # Fill remaining length
        remaining_length = length - len(password)
        if remaining_length < 0:
            messagebox.showerror("Error", "Password length too short for required character types.")
            return
            
        password.extend(random.choice(char_pool) for _ in range(remaining_length))
        
        # Shuffle password
        random.shuffle(password)
        password = ''.join(password)
        
        # Update GUI
        self.password_var.set(password)
        self.strength_var.set(f"Strength: {self.check_password_strength(password)}")
    
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showerror("Error", "No password to copy!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()