import tkinter as tk
from tkinter import ttk
from manager.manager import Manager
from logreg import LogRegModals
from tkinter import messagebox



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
            text="Book Ticket",
            font=("Arial", 12),
            bg="white",
            fg="black",
            command=self.handle_login,
        )
        login_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Register Button
        register_button = tk.Button(
            header_frame,
            text="Purchase History",
            font=("Arial", 12),
            bg="white",
            fg="black",
            command=self.show_my_tickets,
        )
        register_button.pack(side=tk.RIGHT, padx=10, pady=20)


        # upcoming_events_button
        upcoming_events_button = tk.Button(
            header_frame,
            text="Upcoming Events",
            font=("Arial", 12),
            bg="white",
            fg="black",
            command=self.handle_register,
        )
        upcoming_events_button.pack(side=tk.RIGHT, padx=10, pady=20)

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

        columns = ("ID","Type", "Description", "Price", "Validity", "Discount", "Limitations")
        ticket_tree = ttk.Treeview(self.content_frame, columns=columns, show="headings", height=10)

        for col in columns:
            ticket_tree.heading(col, text=col)
            ticket_tree.column(col, anchor=tk.CENTER, width=120)

        ticket_tree.pack(fill=tk.BOTH, expand=True)

        # Load tickets into the TreeView
        tickets = self.manager.get_all_tickets()
        for ticket in tickets:
            print(ticket)
            ticket_tree.insert(
                "", "end", values=(ticket[0],ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], ticket[6])
            )

        # Create a booking frame for actions
        booking_frame = tk.Frame(self.content_frame, bg="white")
        booking_frame.pack(fill=tk.X, pady=10)

        # Label for selecting an event
        action_label = tk.Label(
            booking_frame,
            text="Select an event and click Book:",
            font=("Arial", 12),
            bg="white",
        )
        action_label.pack(side=tk.LEFT, padx=10)

        # Button for booking
        book_button = tk.Button(
            booking_frame,
            text="Purchase Ticket",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=lambda: self.purchase_ticket(ticket_tree)
        )
        book_button.pack(side=tk.RIGHT, padx=10)

    def show_my_tickets(self):
        """Display available tickets."""
        self.clear_content_frame()
        self.current_display = "mytickets"

        tickets_label = tk.Label(
            self.content_frame,
            text="Purchased Tickets",
            font=("Arial", 18, "bold"),
            bg="white",
        )
        tickets_label.pack(anchor=tk.W, pady=10)

        columns = ("ID","Type", "Description", "Price", "Validity", "Discount", "Limitations","Exp Date","# Tickets")
        ticket_tree = ttk.Treeview(self.content_frame, columns=columns, show="headings", height=10)

        for col in columns:
            ticket_tree.heading(col, text=col)
            ticket_tree.column(col, anchor=tk.CENTER, width=120)

        ticket_tree.pack(fill=tk.BOTH, expand=True)

        # Load tickets into the TreeView
        tickets = self.manager.get_user_tickets(LogRegModals.get_current_user())
        
        if tickets:
            for ticket in tickets:
                print(ticket)
                ticket_tree.insert(
                    "", "end", values=(ticket[0],ticket[1], ticket[2], 
                                    ticket[3], ticket[4], ticket[5], ticket[6],ticket[7],ticket[8])
                )

        # Create a booking frame for actions
        booking_frame = tk.Frame(self.content_frame, bg="white")
        booking_frame.pack(fill=tk.X, pady=10)

        # Label for selecting an event
        action_label = tk.Label(
            booking_frame,
            text="Select an event and click Action:",
            font=("Arial", 12),
            bg="white",
        )
        action_label.pack(side=tk.LEFT, padx=10)

        # Button for booking
        edit_button = tk.Button(
            booking_frame,
            text="Edit",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=lambda: self.edit_ticket(ticket_tree)
        )
        edit_button.pack(side=tk.RIGHT, padx=10)

        # Button for booking
        delete_button = tk.Button(
            booking_frame,
            text="Delete",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=lambda: self.delete_ticket(ticket_tree)
        )
        delete_button.pack(side=tk.RIGHT, padx=10)

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

        # Define columns for the Treeview
        columns = ("ID", "Name", "Description", "Date", "Time", "Capacity")
        event_tree = ttk.Treeview(self.content_frame, columns=columns, show="headings", height=10)

        # Configure columns
        for col in columns:
            event_tree.heading(col, text=col)
            event_tree.column(col, anchor=tk.CENTER, width=120)

        # Add Treeview to the frame
        event_tree.pack(fill=tk.BOTH, expand=True)

        # Load events into the Treeview
        events = self.manager.get_all_events()
        if isinstance(events, list):
            for event in events:
                event_tree.insert("", "end", values=tuple(event))

        # Create a booking frame for actions
        booking_frame = tk.Frame(self.content_frame, bg="white")
        booking_frame.pack(fill=tk.X, pady=10)

        # Label for selecting an event
        action_label = tk.Label(
            booking_frame,
            text="Select an event and click Book:",
            font=("Arial", 12),
            bg="white",
        )
        action_label.pack(side=tk.LEFT, padx=10)

        # Button for booking
        book_button = tk.Button(
            booking_frame,
            text="Book",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=lambda: self.book_event(event_tree)
        )
        book_button.pack(side=tk.RIGHT, padx=10)


    def create_modal_window(self,parent, title, width, height, bg_color="white", modal=True, resizable=False):
        """Creates and returns a reusable modal window."""
        modal_window = tk.Toplevel(parent)
        modal_window.title(title)
        modal_window.geometry(f"{width}x{height}")
        modal_window.configure(bg=bg_color)

        if modal:
            modal_window.grab_set()  # Make it modal

        if not resizable:
            modal_window.resizable(False, False)  # Disable resizing

        modal_window.attributes("-toolwindow", True)  # Disable minimize/maximize
        return modal_window
    


    def book_event(self, event_tree):
        """Handle the booking process for the selected event."""
        selected_item = event_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an event to book!")
            return

        event_details = event_tree.item(selected_item, "values")
        event_id = event_details[0]  # Assuming the first column is Event ID

        # Prompt for the number of tickets
        def submit_booking():
            num_tickets = ticket_entry.get()
            if not num_tickets.isdigit() or int(num_tickets) <= 0:
                messagebox.showerror("Error", "Please enter a valid number of tickets!")
                return
            
            # Call the manager to handle booking logic
            success_message = self.manager.add_ticket(LogRegModals.curremt_user, event_id, int(num_tickets))
            messagebox.showinfo("Success", success_message)
            booking_window.destroy()

        # Open a modal for ticket input
        booking_window = self.create_modal_window(self.content_frame, "Book Tickets", 300, 200, bg_color="white")

        tk.Label(
            booking_window,
            text=f"Book tickets for Event ID: {event_id}",
            font=("Arial", 12),
            bg="white",
        ).pack(pady=10)

        tk.Label(
            booking_window,
            text="Number of Tickets:",
            font=("Arial", 10),
            bg="white",
        ).pack(anchor=tk.W, padx=20)

        ticket_entry = tk.Entry(booking_window, font=("Arial", 12))
        ticket_entry.pack(pady=10, padx=20, fill=tk.X)

        tk.Label(
            booking_window,
            text="Ticket Type:",
            font=("Arial", 10),
            bg="white",
        ).pack(anchor=tk.W, padx=20)

        # Dropdown for ticket type
        ticket_type_var = tk.StringVar()
        ticket_type_dropdown = ttk.Combobox(
            booking_window,
            textvariable=ticket_type_var,
            values=["Single-Day Pass", "Two-Day Pass", "Premium"],  # Add ticket types here
            font=("Arial", 12),
            state="readonly",  # Prevent user from entering custom values
        )
        ticket_type_dropdown.pack(pady=10, padx=20, fill=tk.X)

        submit_button = tk.Button(
            booking_window,
            text="Submit",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=submit_booking,
        )
        submit_button.pack(pady=10)

    '''
    Help user to edit a ticket, by changing number
    '''
    def edit_ticket(self, ticket_tree):
        """Handle the editing process for the selected ticket."""
        selected_item = ticket_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an Ticket to modify")
            return

        ticket_details = ticket_tree.item(selected_item, "values")
        ticket_id = ticket_details[0]  # Assuming the first column is Event ID

        # Prompt for the number of tickets
        def submit_edit():
            num_tickets = ticket_entry.get()
            if not num_tickets.isdigit() or int(num_tickets) <= 0:
                messagebox.showerror("Error", "Please enter a valid number of tickets!")
                return
            
            # Call the manager to handle booking logic
            success_message = self.manager.edit_ticket(LogRegModals.get_current_user(), ticket_id, int(num_tickets))
            messagebox.showinfo("Success", success_message)
            booking_window.destroy()

        # Open a modal for ticket input
        booking_window = self.create_modal_window(self.content_frame, "Edit Tickets", 300, 200, bg_color="white")

        tk.Label(
            booking_window,
            text=f"Edit ticket ID: {ticket_id}",
            font=("Arial", 12),
            bg="white",
        ).pack(pady=10)

        tk.Label(
            booking_window,
            text="Number of Tickets:",
            font=("Arial", 10),
            bg="white",
        ).pack(anchor=tk.W, padx=20)

        ticket_entry = tk.Entry(booking_window, font=("Arial", 12))
        ticket_entry.pack(pady=10, padx=20, fill=tk.X)


        submit_button = tk.Button(
            booking_window,
            text="Submit",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=submit_edit,
        )
        submit_button.pack(pady=10)

    '''
    Method for purchasing a ticket, display a modal to prompt number of tickets
    '''
    def purchase_ticket(self, event_tree):
        """Handle the purchase process for the selected event."""
        selected_item = event_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an event to book!")
            return

        event_details = event_tree.item(selected_item, "values")
        event_id = event_details[0]  # Assuming the first column is Event ID

        # Prompt for the number of tickets
        def submit_purchase():
            num_tickets = ticket_entry.get()
            if not num_tickets.isdigit() or int(num_tickets) <= 0:
                messagebox.showerror("Error", "Please enter a valid number of tickets!")
                return
            
            # Call the manager to handle booking logic
            success_message = self.manager.add_ticket(LogRegModals.get_current_user(), int(event_id), int(num_tickets))
            messagebox.showinfo("Success", success_message)
            booking_window.destroy()

        # Open a modal for ticket input
        booking_window = self.create_modal_window(self.content_frame, "Purchase Tickets", 300, 200, bg_color="white")

        tk.Label(
            booking_window,
            text=f"Book  Ticket ID: {event_id}",
            font=("Arial", 12),
            bg="white",
        ).pack(pady=10)

        tk.Label(
            booking_window,
            text="Number of Tickets:",
            font=("Arial", 10),
            bg="white",
        ).pack(anchor=tk.W, padx=20)

        ticket_entry = tk.Entry(booking_window, font=("Arial", 12))
        ticket_entry.pack(pady=10, padx=20, fill=tk.X)

        submit_button = tk.Button(
            booking_window,
            text="Submit",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=submit_purchase,
        )
        submit_button.pack(pady=10)

    '''
    Method for delete a ticket, display a modal to prompt number of tickets
    '''
    def delete_ticket(self, ticket_tree):
        """Handle the purchase process for the selected event."""
        selected_item = ticket_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select ticket to delete!")
            return

        ticket_details = ticket_tree.item(selected_item, "values")
        ticket_id = ticket_details[0]  # Assuming the first column is Event ID

        # Prompt for the number of tickets
        def submit_delete():
            # Call the manager to handle booking logic
            success_message = self.manager.delete_ticket(LogRegModals.get_current_user(), int(ticket_id))
            messagebox.showinfo("Success", success_message)
            booking_window.destroy()

        # Open a modal for ticket input
        booking_window = self.create_modal_window(self.content_frame, " Delete Ticket", 300, 200, bg_color="white")

        tk.Label(
            booking_window,
            text=f"Delete  Ticket ID: {ticket_id}",
            font=("Arial", 12),
            bg="white",
        ).pack(pady=10)

        tk.Label(
            booking_window,
            text="Confirm Ticket ID:",
            font=("Arial", 10),
            bg="white",
        ).pack(anchor=tk.W, padx=20)

        ticket_entry = tk.Entry(booking_window, font=("Arial", 12))
        ticket_entry.pack(pady=10, padx=20, fill=tk.X)

        submit_button = tk.Button(
            booking_window,
            text="Submit",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=submit_delete,
        )
        submit_button.pack(pady=10)

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
        "id": "01",
        "Type": "Single-Day Pass",
        "Description": "Access to the park for one day",
        "Price": "275 DHS",
        "Validity": "1 Day",
        "Discount": "None",
        "Limitations": "Valid only on selected date",
    },
    {
        "id": "02",
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

    ##for testing
    print(manager.add_user(LogRegModals.get_current_user()))

    
    for event in events:  # Add mock events to the manager
        ev = manager.add_event(event)
        print(ev)

    for ticket in tickets:
            print(ticket)
            new_ticket = manager.load_tickets(
                ticket_type=ticket["Type"],
                description=ticket["Description"],
                price=ticket["Price"],
                validity=ticket["Validity"],
                discount=ticket["Discount"],
                limitations=ticket["Limitations"],
            )
            print(new_ticket)
            

    root = tk.Tk()
    app = TicketManagerApp(root, manager)
    root.mainloop()
