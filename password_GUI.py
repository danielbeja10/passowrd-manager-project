import customtkinter as ctk
import json
import os

PASSWORDS_FILE = "Passwords.json"

class PasswordManagerGUI:
    def __init__(self):
        self.init_password_file()
        self.build_gui()

    def init_password_file(self):
        if not os.path.exists(PASSWORDS_FILE):
            with open(PASSWORDS_FILE, "w", encoding="utf-8") as f:
                json.dump({}, f, indent=2)

    def build_gui(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.app = ctk.CTk()
        self.app.title("Password Manager")
        self.app.geometry("400x400")

        self.site_entry = ctk.CTkEntry(self.app, placeholder_text="Site name")
        self.site_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self.app, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10)

        self.add_button = ctk.CTkButton(self.app, text="Add", command=self.add_password)
        self.add_button.pack(pady=5)

        self.get_button = ctk.CTkButton(self.app, text="Get", command=self.get_password)
        self.get_button.pack(pady=5)

        self.remove_button = ctk.CTkButton(self.app, text="Remove", command=self.remove_password)
        self.remove_button.pack(pady=5)

        self.status_label = ctk.CTkLabel(self.app, text="")
        self.status_label.pack(pady=10)

        self.app.mainloop()

    def load_passwords(self):
        with open(PASSWORDS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_passwords(self, passwords):
        with open(PASSWORDS_FILE, "w", encoding="utf-8") as f:
            json.dump(passwords, f, indent=2, ensure_ascii=False)

    def add_password(self):
        site = self.site_entry.get().strip()
        password = self.password_entry.get().strip()

        if not site or not password:
            self.status_label.configure(text="Please enter both site and password.")
            return

        passwords = self.load_passwords()
        passwords[site] = password
        self.save_passwords(passwords)

        self.s
