import tkinter as tk
from tkinter import ttk
from manager.manager import Manager
from logreg import LogRegModals
from data import load_or_create_data
from models.user import User
from models.ticket import Ticket
from models.event import Event
from clientDashBoard import TicketManagerApp as CTA
from adminDashBoard import TicketManagerApp as ATA

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

        columns = ("ID","Type", "Description", "Price", "Validity", "Discount", "Limitations")
        ticket_tree = ttk.Treeview(self.content_frame, columns=columns, show="headings", height=10)

        for col in columns:
            ticket_tree.heading(col, text=col)
            ticket_tree.column(col, anchor=tk.CENTER, width=120)

        ticket_tree.pack(fill=tk.BOTH, expand=True)

        # Load tickets into the TreeView
        tickets = self.manager.get_all_tickets()
        print("-------- all tickets --")
        print(tickets)
        for ticket in tickets:
            ticket_tree.insert(
                "", "end", values=(ticket[0],ticket[1], ticket[2], ticket[3], ticket[4], ticket[5], ticket[6])
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
        result = LogRegModals.create_login_window(self.root,self.manager)
        user = LogRegModals.get_current_user()

        if result:
            self.root.quit() 
            if user.get_name() == "admin":
                ATA.show_dashboard(self.root,self.manager)
            else:
                CTA.show_dashboard(self.root,self.manager)
        print("---------------->",result)
       

    def handle_register(self):
        print("Register button clicked!")
        result = LogRegModals.create_register_window(self.root,self.manager)
        if result:
            self.root.quit() 
            CTA.show_dashboard(self.root,self.manager)
        print("---------------->",result)
           
        

# Main
if __name__ == "__main__":
    manager = Manager()
    tickets, events, users , ph = load_or_create_data()

    for user in users.values():
        if isinstance(user, User):
            ev = manager.add_user(user)
        
    
    for event in events.values(): 
        print(event.display_details())
        ev = manager.add_event_data(event)
        print(ev)

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
            
            
   
    
    manager._purchase_history = ph

    for p in ph:
        print("------------------------ph -----------------")
        print(p)

    root = tk.Tk()
    app = TicketManagerApp(root, manager)

    root.protocol("WM_DELETE_WINDOW", manager.save_data_to_file())
    root.mainloop()
