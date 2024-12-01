import tkinter as tk
from tkinter import ttk
from manager.manager import Manager
from logreg import LogRegModals


class TicketManagerApp:
    def __init__(self, root, manager):
        self.root = root
        self.manager = manager
        self.root.title("Ticket Management System")
        self.root.geometry("800x600")
        self.root.configure(bg="#f4f4f4")

        # Header
        self.create_header()

        # Ticket Display
        self.create_ticket_display()

    def create_header(self):
        header_frame = tk.Frame(self.root, bg="#3b5998", height=80)
        header_frame.pack(fill=tk.X)

        title_label = tk.Label(
            header_frame,
            text="Ticket Management System",
            font=("Arial", 24, "bold"),
            bg="#3b5998",
            fg="white",
        )
        title_label.pack(side=tk.LEFT, padx=20)

        login_button = tk.Button(
            header_frame,
            text="Login",
            font=("Arial", 12),
            bg="white",
            fg="black",
            command=self.handle_login,
        )
        login_button.pack(side=tk.RIGHT, padx=10, pady=20)

        register_button = tk.Button(
            header_frame,
            text="Register",
            font=("Arial", 12),
            bg="white",
            fg="black",
            command=self.handle_register,
        )
        register_button.pack(side=tk.RIGHT, padx=10, pady=20)

    def create_ticket_display(self):
        ticket_frame = tk.Frame(self.root, bg="white", padx=10, pady=10)
        ticket_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tickets_label = tk.Label(
            ticket_frame,
            text="Available Tickets",
            font=("Arial", 18, "bold"),
            bg="white",
        )
        tickets_label.pack(anchor=tk.W, pady=10)

        columns = ("Type", "Description", "Price", "Validity", "Discount", "Limitations")
        ticket_tree = ttk.Treeview(ticket_frame, columns=columns, show="headings", height=10)

        for col in columns:
            ticket_tree.heading(col, text=col)
            ticket_tree.column(col, anchor=tk.CENTER, width=120)

        ticket_tree.pack(fill=tk.BOTH, expand=True)

        # Load tickets into the TreeView
        tickets = self.manager._tickets
        for ticket in tickets:
            ticket_tree.insert(
                "", "end", values=(ticket['Type'], ticket['Description'], ticket['Price'], ticket['Validity'], ticket['Discount'], ticket['Limitations'])
            )

    def handle_login(self):
        print("Login button clicked!")
        LogRegModals.create_login_window(self.root)

    def handle_register(self):
        print("Register button clicked!")
        LogRegModals.create_register_window(self.root)


# Mock Data
tickets = [
    {
        "Type": "Single-Day Pass",
        "Description": "Access to the park for one day",
        "Price": "275 DHS",
        "Validity": "1 Day",
        "Discount": "None",
        "Limitations": "Valid only on selected date",
    },
    {
        "Type": "Two-Day Pass",
        "Description": "Access to the park for two consecutive days",
        "Price": "480 DHS",
        "Validity": "2 Days",
        "Discount": "10% online discount",
        "Limitations": "Cannot split over multiple trips",
    },
    # Add more ticket data here...
]

# Main
if __name__ == "__main__":
    manager = Manager()
    manager._tickets = tickets  # Add mock tickets to the manager

    root = tk.Tk()
    app = TicketManagerApp(root, manager)
    root.mainloop()
