import tkinter as tk
from tkinter import messagebox


class LogRegModals:
    @staticmethod
    def create_register_window(parent):
        """Creates the Register modal window."""
        def submit_registration():
            username = username_entry.get()
            email = email_entry.get()
            password = password_entry.get()
            if username and email and password:
                messagebox.showinfo("Success", f"User '{username}' registered successfully!")
                register_window.destroy()
            else:
                messagebox.showerror("Error", "All fields are required!")

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

    @staticmethod
    def create_login_window(parent):
        """Creates the Login modal window."""
        def submit_login():
            email = email_entry.get()
            password = password_entry.get()
            if email and password:
                messagebox.showinfo("Success", f"Welcome back!")
                login_window.destroy()
            else:
                messagebox.showerror("Error", "Both fields are required!")

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
