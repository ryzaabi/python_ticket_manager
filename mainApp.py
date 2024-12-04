import tkinter as tk
from tkinter import ttk, messagebox
from manager.manager import Manager
from data import load_or_create_data
from models.user import User



class TicketManagerApp:
    def __init__(self, root, manager):
        self.root = root
        self.manager = manager
        self.root.title("Ticket Management System")
        self.root.geometry("800x600")
        self.root.configure(bg="#f4f4f4")

        # Container Frame for Dynamic Scene Management
        self.container = tk.Frame(self.root)
        self.container.pack(side=tk.BOTTOM,fill=tk.BOTH, expand=True)

        self.current_user = None  # To track the logged-in user
        self.header_frame = None  # To track the header
        self.show_login()

    def get_header(self,user_name):
        if user_name == "admin":
            return self.create_header(
            "Ticket Management System - Admin",
            [
                ("Tickets", self.show_tickets_admin),
                ("Sold Tickets", self.show_purchased_tickets),
                ("Events", self.show_events_admin),
                ("Booked Events", self.show_booked_events_admin),
                ("Users", self.show_users),
                ("Logout", self.handle_logout),
            ],
            )
        else:
            return self.create_header(
            "Ticket Management System - Client",
            [
                ("Tickets", self.show_tickets_client),
                ("Events", self.show_events_client),
                ("Booked Events", self.show_booked_events_client),
                ("Purchased Tickets", self.show_my_tickets),
                ("Logout", self.handle_logout),
            ],
            )

    def create_action_frame(self, parent, label_text, buttons):
        """
        Create a reusable action frame with a label and buttons.
        
        :param parent: The parent frame where the action frame will be added.
        :param label_text: The text for the action label.
        :param buttons: A list of tuples where each tuple contains:
                        (button_text, button_command)
        """
        # Create the action frame
        action_frame = tk.Frame(parent, bg="white")
        action_frame.pack(fill=tk.X, pady=10)

        # Add the label
        action_label = tk.Label(
            action_frame,
            text=label_text,
            font=("Arial", 12),
            bg="white",
        )
        action_label.pack(side=tk.LEFT, padx=10)

        # Add buttons dynamically
        for button_text, button_command in buttons:
            tk.Button(
                action_frame,
                text=button_text,
                font=("Arial", 12),
                bg="#4CAF50",
                fg="white",
                command=button_command,
            ).pack(side=tk.RIGHT, padx=10)  


    def clear_container(self):
        """Clear all widgets from the container."""
        for widget in self.container.winfo_children():
            widget.destroy()

    def create_header(self, title, buttons):
        """
        Create a reusable header that always appears at the top.
        
        :param title: Title text for the header.
        :param buttons: List of tuples (button_text, button_command) for the header buttons.
        """

        if self.header_frame:
            self.header_frame.destroy()

        self.header_frame = tk.Frame(self.root, bg="#3b5998", height=80)
        self.header_frame.pack(side=tk.TOP,fill=tk.X)

        # Title
        title_label = tk.Label(
            self.header_frame,
            text=title,
            font=("Arial", 24, "bold"),
            bg="#3b5998",
            fg="white",
        )
        title_label.pack(side=tk.LEFT, padx=20)

        # Buttons
        for button_text, command in buttons:
            tk.Button(
                self.header_frame,
                text=button_text,
                font=("Arial", 12),
                bg="white",
                fg="black",
                command=command,
            ).pack(side=tk.RIGHT, padx=10, pady=20)

    def show_login(self):
        """Display the login screen."""
        self.clear_container()

        self.create_header(
            "Ticket Management System - Login",
            [
              
            ],
        )

        login_frame = tk.Frame(self.container, bg="#f4f4f4")
        login_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(
            login_frame, text="Login", font=("Arial", 24, "bold"), bg="#f4f4f4"
        ).pack(pady=20)

        tk.Label(login_frame, text="Username:", bg="#f4f4f4").pack(anchor=tk.W, pady=5)
        username_entry = tk.Entry(login_frame, font=("Arial", 14))
        username_entry.pack(fill=tk.X, pady=5)

        tk.Label(login_frame, text="Password:", bg="#f4f4f4").pack(anchor=tk.W, pady=5)
        password_entry = tk.Entry(login_frame, font=("Arial", 14), show="*")
        password_entry.pack(fill=tk.X, pady=5)

        def login_action():
            username = username_entry.get()
            password = password_entry.get()
            luser = None

             # Check if email exists and password matches
            for user in manager._users.values():
                if user.get_name() == username and user.get_password() == password:
                    messagebox.showinfo("Success", f"Welcome, {user.get_name()}!")
                    luser = user
                    break
            if luser:
                self.current_user = user
                if user.get_name() == "admin":
                    self.show_admin_dashboard()
                else:
                    self.show_client_dashboard()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")

        tk.Button(
            login_frame,
            text="Login",
            command=login_action,
            font=("Arial", 14),
            bg="#4CAF50",
            fg="white",
        ).pack(pady=20)

        tk.Button(
            login_frame,
            text="Register",
            command=self.show_register,
            font=("Arial", 12),
            bg="#f4f4f4",
            fg="blue",
        ).pack()

    def show_register(self):
        """Display the registration screen."""
        self.clear_container()

        self.create_header(
            "Ticket Management System - Register",
            [
              
            ],
        )

        register_frame = tk.Frame(self.container, bg="#f4f4f4")
        register_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(
            register_frame, text="Register", font=("Arial", 24, "bold"), bg="#f4f4f4"
        ).pack(pady=20)

        tk.Label(register_frame, text="Username:", bg="#f4f4f4").pack(anchor=tk.W)
        username_entry = tk.Entry(register_frame, font=("Arial", 14))
        username_entry.pack(fill=tk.X, pady=5)

        tk.Label(register_frame, text="email:", bg="#f4f4f4").pack(anchor=tk.W)
        email_entry = tk.Entry(register_frame, font=("Arial", 14))
        email_entry.pack(fill=tk.X, pady=5)

        tk.Label(register_frame, text="Password:", bg="#f4f4f4").pack(anchor=tk.W)
        password_entry = tk.Entry(register_frame, font=("Arial", 14), show="*")
        password_entry.pack(fill=tk.X, pady=5)

        def register_action():
            username = username_entry.get()
            password = password_entry.get()
            email = email_entry.get()
            if self.manager.add_user_data(username, email,password):
                messagebox.showinfo("Success", "Registration successful!")
                self.show_login()
            else:
                messagebox.showerror("Error", "Registration failed. User might exist.")

        tk.Button(
            register_frame,
            text="Register",
            command=register_action,
            font=("Arial", 14),
            bg="#4CAF50",
            fg="white",
        ).pack(pady=20)

        tk.Button(
            register_frame,
            text="Back to Login",
            command=self.show_login,
            font=("Arial", 12),
            bg="#f4f4f4",
            fg="blue",
        ).pack()

    def show_client_dashboard(self):
        """Display the client dashboard."""
        self.clear_container()
        
        self.get_header("client")

        tk.Label(
            self.container,
            text=f"Welcome, {self.current_user.get_name()}!",
            font=("Arial", 18),
            bg="#f4f4f4",
        ).pack(pady=20)

    def show_admin_dashboard(self):
        """Display the admin dashboard."""
        self.clear_container()
        self.get_header("admin")

        tk.Label(
            self.container,
            text=f"Welcome to the Admin Dashboard!",
            font=("Arial", 18),
            bg="#f4f4f4",
        ).pack(pady=20)

    def show_tickets_client(self):
        """Display tickets."""
        self.clear_container()

        self.get_header("client")
        
        self.show_tickets()
       

    def show_tickets_admin(self):
        """Display tickets."""
        self.clear_container()

        self.get_header("admin")
        self.show_tickets()

        
    
    def show_tickets(self):

        tickets_frame = tk.Frame(self.container, bg="#f4f4f4")
        tickets_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(
            tickets_frame, text="Available Tickets", font=("Arial", 18), bg="#f4f4f4"
        ).pack(pady=10)

        tickets = self.manager.get_all_tickets()
        if tickets == "No tickets available.":
            tk.Label(tickets_frame, text=tickets, bg="#f4f4f4").pack(pady=20)
        else:
            columns = ("ID","Type", "Description", "Price", "Validity", "Discount", "Limitations")
            ticket_tree = ttk.Treeview(tickets_frame, columns=columns, show="headings", height=10)
            for col in columns:
                ticket_tree.heading(col, text=col)
                ticket_tree.column(col, anchor=tk.CENTER, width=120)
                
            ticket_tree.pack(fill=tk.BOTH, expand=True)

            for ticket in tickets:
                ticket_tree.insert(
                    "", "end", values=(ticket[0],ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], ticket[6])
                )
        # Use the reusable function for the action frame
        if self.current_user.get_name() == "admin":
            self.create_action_frame(
                parent=tickets_frame,
                label_text="Select a ticket and click Purchase:",
                buttons=[
                    ("Delete", lambda: self.purchase_ticket(ticket_tree)),
                    
                ],
            )
        else:
            self.create_action_frame(
                parent=tickets_frame,
                label_text="Select a ticket and click Purchase:",
                buttons=[
                    ("Purchase Ticket", lambda: self.purchase_ticket(ticket_tree)),
                    
                ],
            )

    def show_purchased_tickets(self):
        # will show tickets puchased in admin
        """Display client tickets."""
        self.clear_container()
        self.get_header("admin")
        tickets = self.manager.get_purchased_tickets()
        columns = ["UID","ID","Type", "Price", "Validity", "Discount", "Limitations","Exp Date","# Tickets"]
        self.show_p_tickets(tickets,columns)

    def show_my_tickets(self):
        """Display client tickets."""
        self.clear_container()
        self.get_header("client")
        # show tickets for this user
        columns = ["ID","Type", "Price", "Validity", "Discount", "Limitations","Exp Date","# Tickets"]
        tickets = self.manager.get_user_tickets(self.current_user)
        self.show_p_tickets(tickets,columns)

    def show_p_tickets(self,tickets,columns):
        
        _frame = tk.Frame(self.container, bg="#f4f4f4")
        _frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(
             _frame, text="My Tickets", font=("Arial", 18), bg="#f4f4f4"
        ).pack(pady=10)

       
        if tickets == "User not found.":
            tk.Label( _frame, text=tickets, bg="#f4f4f4").pack(pady=20)

        elif len(tickets) == 0:
            tk.Label( _frame, text="No Tickets Purchased", bg="#f4f4f4").pack(pady=20)

        else:
            
            ticket_tree = ttk.Treeview( _frame, columns=columns, show="headings", height=10)
            for col in columns:
                ticket_tree.heading(col, text=col)
                ticket_tree.column(col, anchor=tk.CENTER, width=120)
            ticket_tree.pack(fill=tk.BOTH, expand=True)
            ticket_tree.column("ID", width=50, anchor=tk.CENTER)
            

            for ticket in tickets:
                if self.current_user.get_name() == "admin":
                    ticket_tree.insert(
                        "", "end", values=(ticket[0],ticket[1], 
                                        ticket[3], ticket[4], ticket[5], ticket[6],ticket[7],ticket[8],ticket[9])
                    )
                else:
                    ticket_tree.insert(
                        "", "end", values=(ticket[0],ticket[1], 
                                        ticket[3], ticket[4], ticket[5], ticket[6],ticket[7],ticket[8])
                    )


        # Use the reusable function for the action frame
        if self.current_user.get_name() == "admin":
            self.create_action_frame(
                parent=_frame,
                label_text="Select a ticket and click action",
                buttons=[
                    ("Delete", lambda: self.delete_ticket(ticket_tree)),
                    ("Update", lambda: self.update_ticket(ticket_tree))
                ],
            )
        else:
            self.create_action_frame(
                parent=_frame,
                label_text="Select a ticket and click action",
                buttons=[
                    ("Delete", lambda: self.delete_ticket(ticket_tree)),
                    ("Update", lambda: self.update_ticket(ticket_tree))
                ],
            )



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
    

    def create_confirmation_modal(self, parent, title, item_id, id_label, action_command):
        """
        Create a reusable modal for confirming an ID-based action.

        :param parent: The parent frame for the modal.
        :param title: Title of the confirmation modal.
        :param item_id: The ID to confirm.
        :param id_label: Label for the ID (e.g., "Ticket ID").
        :param action_command: Function to execute the action, should accept the item_id.
        """
        # Create the modal window
        confirmation_modal = self.create_modal_window(parent, title, 300, 200, bg_color="white")

        # Display the ID and instructions
        tk.Label(
            confirmation_modal,
            text=f"Confirm {id_label}: {item_id}",
            font=("Arial", 12),
            bg="white",
        ).pack(pady=10)

        tk.Label(
            confirmation_modal,
            text=f"Enter {id_label} to confirm:",
            font=("Arial", 10),
            bg="white",
        ).pack(anchor=tk.W, padx=20)

        # Input for confirmation
        confirmation_entry = tk.Entry(confirmation_modal, font=("Arial", 12))
        confirmation_entry.pack(pady=10, padx=20, fill=tk.X)

        def submit_action():
            # Check if the entered ID matches the expected ID
            entered_id = confirmation_entry.get()
            if str(entered_id) == str(item_id):
                # Perform the action
                success_message = action_command(item_id)
                messagebox.showinfo("Success", success_message)
                confirmation_modal.destroy()
            else:
                messagebox.showerror("Error", f"Invalid {id_label}. Please try again.")

        # Submit button
        tk.Button(
            confirmation_modal,
            text="Submit",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=submit_action,
        ).pack(pady=10)

    def create_edit_modal(self, parent, title, item_id, id_label, action_command):
        """
        Create a reusable modal for confirming an ID-based action.

        :param parent: The parent frame for the modal.
        :param title: Title of the confirmation modal.
        :param item_id: The ID to confirm.
        :param id_label: Label for the ID (e.g., "Ticket ID").
        :param action_command: Function to execute the action, should accept the item_id.
        """
        # Create the modal window
        confirmation_modal = self.create_modal_window(parent, title, 300, 200, bg_color="white")

        # Display the ID and instructions
        tk.Label(
            confirmation_modal,
            text=f"Confirm {id_label}: {item_id}",
            font=("Arial", 12),
            bg="white",
        ).pack(pady=10)

        tk.Label(
            confirmation_modal,
            text=f"Enter {id_label} to Update:",
            font=("Arial", 10),
            bg="white",
        ).pack(anchor=tk.W, padx=20)

        # Input for confirmation
        confirmation_entry = tk.Entry(confirmation_modal, font=("Arial", 12))
        confirmation_entry.pack(pady=10, padx=20, fill=tk.X)

        def submit_action():
            # Perform the action
            entered_count = int(confirmation_entry.get())
            success_message = action_command(item_id,entered_count)
            messagebox.showinfo("Success", success_message)
            confirmation_modal.destroy()
           

        # Submit button
        tk.Button(
            confirmation_modal,
            text="Submit",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=submit_action,
        ).pack(pady=10)

    
    def create_booking_modal(self, parent, title, item_id, id_label, action_command):
        """
        Create a reusable modal for booking.

        :param parent: The parent frame for the modal.
        :param title: Title of the confirmation modal.
        :param item_id: The ID to confirm.
        :param id_label: Label for the ID (e.g., "Ticket ID").
        :param action_command: Function to execute the action, should accept the item_id.
        """
        # Create the modal window
        confirmation_modal = self.create_modal_window(parent, title, 300, 200, bg_color="white")

        # Display the ID and instructions
        tk.Label(
            confirmation_modal,
            text=f"Confirm {id_label}: {item_id}",
            font=("Arial", 12),
            bg="white",
        ).pack(pady=10)

        tk.Label(
            confirmation_modal,
            text=f"Enter {id_label} to Book:",
            font=("Arial", 10),
            bg="white",
        ).pack(anchor=tk.W, padx=20)

        # Input for confirmation
        confirmation_entry = tk.Entry(confirmation_modal, font=("Arial", 12))
        confirmation_entry.pack(pady=10, padx=20, fill=tk.X)

        def submit_action():
            # Perform the action
            ticket_id = int(confirmation_entry.get())
            success_message = action_command(ticket_id,item_id)
            messagebox.showinfo("Success", success_message)
            confirmation_modal.destroy()
           

        # Submit button
        tk.Button(
            confirmation_modal,
            text="Submit",
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            command=submit_action,
        ).pack(pady=10)



    def delete_ticket(self,_tree):
        """
        function used to delete a ticked by client/ admin
        """
        """Handle the process of deleting a ticket."""
        # Get the selected item
        selected_item = _tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a ticket to delete!")
            return

        ticket_details = _tree.item(selected_item, "values")
        ticket_id = ticket_details[0]  # Assuming the first column is the Ticket ID

        # Define the action command
        def perform_delete(ticket_id):
            return self.manager.delete_ticket(self.current_user, int(ticket_id))

        # Open the confirmation modal
        self.create_confirmation_modal(
            parent=self.container,
            title="Delete Ticket",
            item_id=ticket_id,
            id_label="Ticket ID",
            action_command=perform_delete,
        )



    def update_ticket(self,_tree):
        """
        function used to update a ticket, by client or admin
        """
        
        # Get the selected item
        selected_item = _tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a ticket to delete!")
            return

        ticket_details = _tree.item(selected_item, "values")
        ticket_id = ticket_details[0]  # Assuming the first column is the Ticket ID

        # Define the action command
        def perform_update(ticket_id,num_tickets):
            return self.manager.edit_ticket(self.current_user, int(ticket_id),num_tickets)

        # Open the confirmation modal
        self.create_edit_modal(
            parent=self.container,
            title="Update Ticket",
            item_id=ticket_id,
            id_label="Ticket ID",
            action_command=perform_update,
        )


    '''
    Method for purchasing a ticket, display a modal to prompt number of tickets
    '''
    def purchase_ticket(self, event_tree):
        """Handle the purchase process for the selected event."""
        selected_item = event_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a ticket to purchase")
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
            success_message = self.manager.add_ticket(self.current_user, int(event_id), int(num_tickets))
            messagebox.showinfo("Success", success_message)
            booking_window.destroy()

        # Open a modal for ticket input
        booking_window = self.create_modal_window(self.container, "Purchase Tickets", 300, 200, bg_color="white")

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


    def show_users(self):
        """Display all users."""
        self.clear_container()
        self.get_header("admin")

        _frame = tk.Frame(self.container, bg="#f4f4f4")
        _frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(
            _frame, text="Registered Users", font=("Arial", 18), bg="#f4f4f4"
        ).pack(pady=10)

        users = self.manager.get_all_users()
        if users == "No users found.":
            tk.Label(_frame, text=users, bg="#f4f4f4").pack(pady=20)
        else:
            columns = ["UID","Name", "Email", "Password"]
            user_tree = ttk.Treeview(_frame, columns=columns, show="headings", height=10)
            for col in columns:
                user_tree.heading(col, text=col)
                user_tree.column(col, anchor=tk.CENTER, width=120)

            user_tree.pack(fill=tk.BOTH, expand=True)

            for user in users:
                print(user)
                user_tree.insert(
                "", "end", values=(user[0],user[1], user[2]))

        # Use the reusable function for the action frame
        self.create_action_frame(
            parent=_frame,
            label_text="Select a ticket and click action",
            buttons=[
                ("Delete", lambda: self.delete_user(user_tree)),
               
            ],
        )

    def delete_user(self,_tree):
        """
        function used to delete a ticked by client/ admin
        """
        """Handle the process of deleting a ticket."""
        # Get the selected item
        selected_item = _tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a user to delete!")
            return

        user_details = _tree.item(selected_item, "values")
        user_id = user_details[0]  

        # Define the action command
        def perform_delete(user_id):
            return self.manager.delete_user(int(user_id))

        # Open the confirmation modal
        self.create_confirmation_modal(
            parent=self.container,
            title="Remove User",
            item_id=user_id,
            id_label="User ID",
            action_command=perform_delete,
        )

    def show_events_client(self):
        self.clear_container()
        self.get_header("client")
        self.show_events()

    def show_events_admin(self):
        self.clear_container()
        self.get_header("admin")
        self.show_events()

    def show_events(self):
        """Display all events."""

        _frame = tk.Frame(self.container, bg="#f4f4f4")
        _frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(
            self.container, text="Available Events", font=("Arial", 18), bg="#f4f4f4"
        ).pack(pady=10)

        events = self.manager.get_all_events()
        if events == "No events available.":
            tk.Label(_frame, text=events, bg="#f4f4f4").pack(pady=20)
        else:
            columns = ["ID", "Name", "Date", "Time", "Capacity"]
            event_tree = ttk.Treeview(_frame, columns=columns, show="headings", height=10)
            for col in columns:
                event_tree.heading(col, text=col)
            event_tree.pack(fill=tk.BOTH, expand=True)

            for event in events:
                event_tree.insert("", "end", values=tuple(event))

        # Use the reusable function for the action frame
        if self.current_user.get_name() == "admin":
            self.create_action_frame(
                parent=_frame,
                label_text="Select a Event and click action",
                buttons=[
                    ("Delete", lambda: self.delete_event(event_tree)),
                    ("Update", lambda: self.update_event(event_tree))
                ],
            )
        else:
             self.create_action_frame(
                parent=_frame,
                label_text="Select a Event and click action",
                buttons=[
                    ("Book Event", lambda: self.book_event(event_tree)),
                    
                ],
            )

    def show_booked_events_client(self):
        self.clear_container()
        self.get_header("client")
        events = self.manager.get_booked_events(self.current_user)
        self.show_booked_events(events)


    def show_booked_events_admin(self):
        self.clear_container()
        self.get_header("admin")
        events = self.manager.get_all_booked_events()
        self.show_booked_events(events)

    def show_booked_events(self,events):
        """Display all events."""

        print(events)
        _frame = tk.Frame(self.container, bg="#f4f4f4")
        _frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        tk.Label(
            self.container, text="Booked Events", font=("Arial", 18), bg="#f4f4f4"
        ).pack(pady=10)

        
        if events == "No events available.":
            tk.Label(_frame, text=events, bg="#f4f4f4").pack(pady=20)
        else:

            
            columns = ["Ecode","Email", "Name", "Desc", "Date", "Time"]
            event_tree = ttk.Treeview(_frame, columns=columns, show="headings", height=10)
            for col in columns:
                event_tree.heading(col, text=col)
            event_tree.pack(fill=tk.BOTH, expand=True)

            for event in events:
                event_tree.insert("", "end", values=tuple(event))

        # Use the reusable function for the action frame
        if self.current_user.get_name() == "admin":
            self.create_action_frame(
                parent=_frame,
                label_text="Select a Event and click action",
                buttons=[
                    ("Delete", lambda: self.delete_booked_evemt(event_tree)),
                    
                ],
            )
        else:
             self.create_action_frame(
                parent=_frame,
                label_text="Select a Event and click action",
                buttons=[
                    ("Remove Event", lambda: self.delete_booked_evemt(event_tree)),
                    
                ],
            )

    def delete_booked_evemt(self,_tree):
        """
        function used to delete booked event
        """
        
        # Get the selected item
        selected_item = _tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an event to delete!")
            return

        ticket_details = _tree.item(selected_item, "values")
        event_code = ticket_details[0]  # Assuming the first column is the Ticket ID

        # Define the action command
        def perform_delete(event_code):
            
            return self.manager.del_booked_events(self.current_user, event_code)

        # Open the confirmation modal
        self.create_confirmation_modal(
            parent=self.container,
            title="Delete Booked Event",
            item_id=event_code,
            id_label="Event Code",
            action_command=perform_delete,
        )


    def book_event(self,_tree):
        # Get the selected item
        selected_item = _tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select an Event to book!")
            return

        ticket_details = _tree.item(selected_item, "values")
        event_id= ticket_details[0] 

        # Define the action command
        def perform_booking(ticket_id,event_id):
            return self.manager.book_events(self.current_user, int(ticket_id),int(event_id))

        # Open the confirmation modal
        self.create_booking_modal(
            parent=self.container,
            title="Book Event using Ticket",
            item_id=event_id,
            id_label="Event ID",
            action_command=perform_booking,
        )

    def handle_logout(self):
        """Handle logout and return to login screen."""
        self.current_user = None
        self.show_login()


# Main Execution
if __name__ == "__main__":
    manager = Manager()
    tickets, events, users, ph = load_or_create_data()

    for ticket in tickets.values():
            print(ticket)          
            if isinstance(ticket, dict):
                new_ticket = manager.load_tickets(
                    ticket_type=ticket["Type"],
                    description=ticket["Description"],
                    price=ticket["Price"],
                    validity=ticket["Validity"],
                    discount=ticket["Discount"],
                    limitations=ticket["Limitations"],
                )
            else:
                manager.load_tickets_data(ticket)

    for user in users.values():
        manager.add_user(user)

    for event in events.values():
        manager.add_event_data(event)

    manager._purchase_history = ph

    root = tk.Tk()
    app = TicketManagerApp(root, manager)
    root.mainloop()
