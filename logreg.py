import tkinter as tk
from tkinter import messagebox
from models.user import User 
from manager.manager import Manager 

current_user = User(0, "erick", 'erick@gmail.com', "mymum")

class LogRegModals:

    @staticmethod
    def get_current_user():
        return current_user
    
    @staticmethod
    def create_register_window(parent, manager):
        """Creates the Register modal window."""
        success = False
        def submit_registration():
            nonlocal success 
            username = username_entry.get()
            email = email_entry.get()
            password = password_entry.get()

            # Validate input
            if not username or not email or not password:
                messagebox.showerror("Error", "All fields are required!")
                return

            # Check if email already exists
            for user in manager._users.values():
                if user.get_email() == email:
                    messagebox.showerror("Error", "Email already registered!")
                    return

            # Add the new user
            user = User(manager._next_user_id, username, email, password)
            success_message = manager.add_user(user)
            success = True
            LogRegModals.current_user = user #attach user
            messagebox.showinfo("Success", success_message)
            register_window.destroy()
            

        register_window = tk.Toplevel(parent)
        register_window.title("Register")
        register_window.geometry("400x400")
        register_window.configure(bg="#f4f4f4")
        register_window.grab_set()  # Make modal
        register_window.resizable(False, False)  # Disable resize
        register_window.attributes("-toolwindow", True)  # Disable minimize/maximize

        # Header
        header_frame = tk.Frame(register_window, bg="#3b5998", height=60)
        header_frame.pack(fill=tk.X)

        title_label = tk.Label(
            header_frame,
            text="Register",
            font=("Arial", 20, "bold"),
            bg="#3b5998",
            fg="white",
        )
        title_label.pack(padx=20, pady=10)

        # Form Fields
        tk.Label(register_window, text="Username:", bg="#f4f4f4", font=("Arial", 12)).pack(pady=5, anchor=tk.W, padx=20)
        username_entry = tk.Entry(register_window, font=("Arial", 12))
        username_entry.pack(pady=5, padx=20, fill=tk.X)

        tk.Label(register_window, text="Email:", bg="#f4f4f4", font=("Arial", 12)).pack(pady=5, anchor=tk.W, padx=20)
        email_entry = tk.Entry(register_window, font=("Arial", 12))
        email_entry.pack(pady=5, padx=20, fill=tk.X)

        tk.Label(register_window, text="Password:", bg="#f4f4f4", font=("Arial", 12)).pack(pady=5, anchor=tk.W, padx=20)
        password_entry = tk.Entry(register_window, font=("Arial", 12), show="*")
        password_entry.pack(pady=5, padx=20, fill=tk.X)

        # Submit Button
        submit_button = tk.Button(
            register_window,
            text="Submit",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=submit_registration,
        )
        submit_button.pack(pady=10)

        # Close Button
        close_button = tk.Button(
            register_window,
            text="Close",
            font=("Arial", 12),
            bg="#f44",
            fg="white",
            command=register_window.destroy,
        )
        close_button.pack(pady=10)

        register_window.wait_window()
        return success

    @staticmethod
    def create_login_window(parent,manager):
        """Creates the Login modal window."""
        success = False
        def submit_login():
            nonlocal success 
            email = email_entry.get()
            password = password_entry.get()

            # Validate input
            if not email or not password:
                messagebox.showerror("Error", "Both fields are required!")
                return

            # Check if email exists and password matches
            for user in manager._users.values():
                if user.get_email() == email and user.get_password() == password:
                    messagebox.showinfo("Success", f"Welcome, {user.get_name()}!")
                    LogRegModals.current_user = user #attach user
                    success = True
                    login_window.destroy()
                    return

            messagebox.showerror("Error", "Invalid email or password!")

        login_window = tk.Toplevel(parent)
        login_window.title("Login")
        login_window.geometry("400x300")
        login_window.configure(bg="#f4f4f4")
        login_window.grab_set()  # Make modal
        login_window.resizable(False, False)  # Disable resize
        login_window.attributes("-toolwindow", True)  # Disable minimize/maximize

        # Header
        header_frame = tk.Frame(login_window, bg="#3b5998", height=60)
        header_frame.pack(fill=tk.X)

        title_label = tk.Label(
            header_frame,
            text="Login",
            font=("Arial", 20, "bold"),
            bg="#3b5998",
            fg="white",
        )
        title_label.pack(padx=20, pady=10)

        # Form Fields
        tk.Label(login_window, text="Email:", bg="#f4f4f4", font=("Arial", 12)).pack(pady=5, anchor=tk.W, padx=20)
        email_entry = tk.Entry(login_window, font=("Arial", 12))
        email_entry.pack(pady=5, padx=20, fill=tk.X)

        tk.Label(login_window, text="Password:", bg="#f4f4f4", font=("Arial", 12)).pack(pady=5, anchor=tk.W, padx=20)
        password_entry = tk.Entry(login_window, font=("Arial", 12), show="*")
        password_entry.pack(pady=5, padx=20, fill=tk.X)

        # Submit Button
        submit_button = tk.Button(
            login_window,
            text="Submit",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=submit_login,
        )
        submit_button.pack(pady=10)

        # Close Button
        close_button = tk.Button(
            login_window,
            text="Close",
            font=("Arial", 12),
            bg="#f44",
            fg="white",
            command=login_window.destroy,
        )
        close_button.pack(pady=10)

        login_window.wait_window()
        return success
