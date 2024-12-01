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

        # Current Display State
        self.current_display = "tickets"  # Start with tickets

        # Header
        self.create_header()

        # Content Frame (Dynamic for Home and Events)
        self.content_frame = tk.Frame(self.root, bg="white", padx=10, pady=10)
        self.content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Show Default (Tickets)
        self.show_tickets()

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

        # Home Button
        home_button = tk.Button(
            header_frame,
            text="Home",
            font=("Arial", 12),
            bg="white",
            fg="black",
            command=self.show_tickets,
        )
        home_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Events Button
        events_button = tk.Button(
            header_frame,
            text="Events",
            font=("Arial", 12),
            bg="white",
            fg="black",
            command=self.show_events,
        )
        events_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Login Button
        login_button = tk.Button(
            header_frame,
            text="Login",
            font=("Arial", 12),
            bg="white",
            fg="black",
            command=self.handle_login,
        )
        login_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Register Button
        register_button = tk.Button(
            header_frame,
            text="Register",
            font=("Arial", 12),
            bg="white",
            fg="black",
            command=self.handle_register,
        )
        register_button.pack(side=tk.RIGHT, padx=10, pady=20)

    def show_tickets(self):
        """Display available tickets."""
        self.clear_content_frame()
        self.current_display = "tickets"

        tickets_label = tk.Label(
            self.content_frame,
            text="Available Tickets",
            font=("Arial", 18, "bold"),
            bg="white",
        )
        tickets_label.pack(anchor=tk.W, pady=10)

        columns = ("Type", "Description", "Price", "Validity", "Discount", "Limitations")
        ticket_tree = ttk.Treeview(self.content_frame, columns=columns, show="headings", height=10)

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

    def show_events(self):
        """Display available events."""
        self.clear_content_frame()
        self.current_display = "events"

        events_label = tk.Label(
            self.content_frame,
            text="Available Events",
            font=("Arial", 18, "bold"),
            bg="white",
        )
        events_label.pack(anchor=tk.W, pady=10)

        columns = ("ID", "Name", "Description", "Date", "Time", "Capacity")
        event_tree = ttk.Treeview(self.content_frame, columns=columns, show="headings", height=10)

        for col in columns:
            event_tree.heading(col, text=col)
            event_tree.column(col, anchor=tk.CENTER, width=120)

        event_tree.pack(fill=tk.BOTH, expand=True)

        # Load events into the TreeView
        events = self.manager.get_all_events()
        if isinstance(events, list):
            for event in events:
                event_tree.insert("", "end", values=tuple(event))

    def clear_content_frame(self):
        """Clear the content frame for dynamic switching."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

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
]

events = [
    {
        
        "name": "Music Festival",
        "description": "An amazing music event",
        "date": "2024-12-10",
        "time": "6:00 PM",
        "capacity": 500,
    },
    {
        
        "name": "Food Carnival",
        "description": "Delicious cuisines from around the world",
        "date": "2024-12-15",
        "time": "12:00 PM",
        "capacity": 300,
    },
]

# Main
if __name__ == "__main__":
    manager = Manager()
    manager._tickets = tickets  # Add mock tickets to the manager
    for event in events:  # Add mock events to the manager
        ev = manager.add_event(event)
        print(ev)

    root = tk.Tk()
    app = TicketManagerApp(root, manager)
    root.mainloop()