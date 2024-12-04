
from models.reservation import Reservation
from models.event import Event
from manager.utils import *
from models.ticket import Ticket
from data import *
from models.user import User
import random


class Manager:
    def __init__(self):
        self._users = {}
        self._tickets = []
        self._reserved_tickets = []
        self._reservations = {}
        self._events = {}
        self._purchase_history = []
        self._booked_events = []
        self._next_user_id = 1
        self._next_reservation_id = 1
        self._next_event_id = 1
        self._next_ticket_id = 1
        #for testing
        

    # User Management
    def add_user(self, user):
        user_id = self._next_user_id
        self._users[user_id] = user
        self._next_user_id += 1
        result = f"User '{user.get_name()}' added successfully with ID {user_id}."
        print(result)
        return result
    
    
    def add_user_data(self, name, email,password):
        user_id = self._next_user_id
        new_user = User(user_id, name, email, password)
        self._users[user_id] = new_user
        self._next_user_id += 1
        return f"User '{new_user.get_name()}' added successfully with ID {user_id}."

    def get_user(self, user_id):
        user = self._users.get(user_id)
        return user.display_details() if user else "User not found."
    
    def delete_user(self, user_id):
        for  u in self._users.values():
            if u.get_user_id() == user_id:
                user_found = 1
                del self._users[user_id]
                return f"User {u.get_name()} (ID: {user_id}) has been successfully deleted."

            
        return "User not found."


    def get_all_users(self):
        if not self._users:
            return "No users found."
        return [user.display_details() for user in self._users.values()]

    # Ticket Management

    def load_tickets(self,ticket_type,description,price,validity,discount,
                limitations):
        new_ticket = Ticket(
                ticket_id =  self._next_ticket_id,
                ticket_type=ticket_type,
                description=description,
                price=price,
                validity=validity,
                discount = discount,
                limitations = limitations
            )
        self._tickets.append(new_ticket)
        self._next_ticket_id += 1

    def load_tickets_data(self,ticket):
        self._tickets.append(ticket)
        self._next_ticket_id += 1

    def get_all_tickets(self):
        """Get a list of all available tickets."""
        print("-------------- all tickets manager ---------")
        all_tickets = []
        for ticket in self._tickets:
            if isinstance(ticket, Ticket):
                all_tickets.append(ticket.display_details())

        return all_tickets

    def find_ticket_by_id(self, ticket_id):
        """Find a ticket by its ID."""
        for ticket in self._tickets:
            if ticket.get_ticket_id() == ticket_id:  # Assuming 'Type' acts as the ID
                return ticket
        return None
    

    def add_ticket(self, user, ticket_id,num_tickets):
        # Check if the user exists in the system
        user_found = 0
        print(user.display_details())
        print("---------------> ",user)
        for  u in self._users.values():
            print(u.display_details())
            if u.get_user_id() == user.get_user_id():
                user_found = 1
                break

        if user_found == 0:
            return "User not found."
        
        # Search for the ticket with the given ticket_id
        ticket = None
        for t in self._tickets:
            print(t.display_details())
            if t.get_ticket_id() == ticket_id:
                ticket = t
                break

        # If no ticket is found, return an error message
        if not ticket:
            return f"Ticket with ID {ticket_id} not found."

        expiry_date, error = calculate_expiry(ticket.get_validity())

        if error:
            return error

        # Add the ticket to the user's purchase history
        ticket_data = {
            "uid":user.get_user_id(),
            "ticket": ticket,
            "expiry": expiry_date,
            "num_tickets": num_tickets
        }
        self._purchase_history.append(ticket_data)

        return f"Ticket with ID {ticket_id} added for user {user.get_name()}."

    def edit_ticket(self, user,ticket_id,num_tickets):
        user_found = 0
        for  u in self._users.values():
            if u.get_user_id() == user.get_user_id():
                user_found = 1
                break

        if user_found == 0:
            return "User not found."
        
        if self._purchase_history:
            for d in self._purchase_history:
                if d['uid'] == user.get_user_id():
                    if d['ticket'].get_ticket_id() == ticket_id:
                        d["num_tickets"] = num_tickets
                        return f"Ticket ID {ticket_id} successfully edited Ticket for user {user.get_name()}."
                else:
                    print(d.values(),d['uid'],user.get_user_id())
        return "success"
    
    def delete_ticket(self, user,ticket_id):
        user_found = 0
        for  u in self._users.values():
            if u.get_user_id() == user.get_user_id():
                user_found = 1
                break

        if user_found == 0:
            return "User not found."
        
        if self._purchase_history:
            for d in self._purchase_history:
                if d['uid'] == user.get_user_id():
                    if d['ticket'].get_ticket_id() == ticket_id:
                        self._purchase_history.remove(d)  # Remove the ticket entry
                        return f"Ticket ID {ticket_id} successfully deleted for user {user.get_name()}."
                
        return "success"

    def get_user_tickets(self, user):
        user_found = 0
        for  u in self._users.values():
            if u.get_user_id() == user.get_user_id():
                user_found = 1
                break

        if user_found == 0:
            return "User not found."

        data = []
        print(self._purchase_history)
        if self._purchase_history:
            for d in self._purchase_history:
                if d['uid'] == user.get_user_id():
                    ticket_d =  d['ticket'].display_details()
                    ticket_d.append(d['expiry'])
                    ticket_d.append(d['num_tickets'])
                    data.append(ticket_d)
            print(data)
            return data
        return []
        
    def get_purchased_tickets(self):
        data = []
        if self._purchase_history:
            for d in self._purchase_history:
                ticket_d =  d['ticket'].display_details()
                ticket_d.insert(0, d['uid'])
                ticket_d.append(d['expiry'])
                ticket_d.append(d['num_tickets'])
                data.append(ticket_d)
        return data
            

    # Reservation Management
    def make_reservation(self, user, ticket, visit_date):
        if user.get_user_id() in self._users:
            reservation_id = self._next_reservation_id
            reservation = Reservation(reservation_id, user.get_user_id(), visit_date, ticket)
            self._reservations[reservation_id] = reservation
            self._next_reservation_id += 1
            return f"Reservation {reservation_id} created for user {user.get_name()}."
        return "User not found."
    
    # Reservation Management
   

    def generate_random_value(self):
        # Generate three random letters
        letters = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(3))
        # Generate three random numbers
        numbers = ''.join(random.choice('0123456789') for _ in range(3))
        # Combine letters and numbers
        return letters + numbers

    def book_events(self, user, ticket_id, event_id):
        booking = []
        print(user.get_name())
        user_found = 0
        for  u in self._users.values():
            if u.get_user_id() == user.get_user_id():
                user_found = 1
                break

        if user_found == 0:
            return "User not found."
        
        print(self._purchase_history)
        for d in self._purchase_history:
            if d['uid'] == user.get_user_id():
                if d['ticket'].get_ticket_id() == ticket_id:
                    if int(d["num_tickets"]) >= 1:
                        num = self.generate_random_value()
                        d["num_tickets"] = int(d["num_tickets"]) - 1
                        booking.append(user.get_user_id())
                        booking.append(num)
                        booking.append(event_id)
                        self._booked_events.append(booking)
                        print(self._booked_events)
                        return f"Ticket ID {ticket_id} successfully used for Event {event_id}."
                    else:
                        return "Failed.. No enough tickets"
                else:
                    print("Tickets dont match",ticket_id,event_id)
                    
        return "Failed to book"
    
    def get_booked_events(self,user):
        """
        retrieve all booked event s for a user
        """
        if user.get_user_id() in self._users:
            user_bookings = []
            for b in self._booked_events:
                if b[0] == user.get_user_id():
                    user_bookings.append(b)

            all_books = []
            if len(user_bookings) > 0:
                for b in user_bookings:
                    user = self.get_user(b[0])
                    print(user)
                    event = self.get_event_by_id(b[2])
                    event_code = b[1]
                    valid_book = []
                    valid_book.append(event_code)
                    valid_book.append(user[2])
                    for a in event:
                        valid_book.append(a)
                    all_books.append(valid_book)
                return all_books

            else:
                return []
        else:
            return "user not found"
        
    def del_booked_events(self, user, event_code):
        """
        Remove a booked event for a user based on user ID and event ID.
        """
        if user.get_user_id() in self._users and user.get_name() != "admin":
            # Find the event to remove
            for b in self._booked_events:
                if b[0] == user.get_user_id() and b[1] == event_code:
                    self._booked_events.remove(b)
                    return "Event successfully removed"
            return "Event not found for the user"
        
        elif user.get_name() == "admin":
            for b in self._booked_events:
                if  b[1] == event_code:
                    self._booked_events.remove(b)
                    return "Event successfully removed"

        else:
            return "User not found"

        
    def get_all_booked_events(self):
        """
        retrieve all booked event s for a user
        """
        all_books = []
        if len(self._booked_events) > 0:
            for b in self._booked_events:
                user = self.get_user(b[0])
                event = self.get_event_by_id(b[2])
                event_code = b[1]
                valid_book = []
                valid_book.append(event_code)
                valid_book.append(user[2])
                for a in event:
                        valid_book.append(a)
                all_books.append(valid_book)
            return all_books

        else:
            return []
        


    def get_user_reservations(self, user):
        if user.get_user_id() in self._users:
            return [
                res.display_details() for res in self._reservations.values()
                if res.get_user_id() == user.get_user_id()
            ]
        return "User not found."

    # Event Management
    def add_event(self, name, description, date, time, capacity):
        event_id = self._next_event_id
        event = Event(event_id, name, description, date, time, capacity)
        self._events[event_id] = event
        self._next_event_id += 1
        return f"Event '{name}' added with ID {event_id}."
    
    # Event Management
    def add_event_data(self, event):
        event_id = self._next_event_id
        self._events[event_id] = event
        self._next_event_id += 1
        return f"Event '{event.display_details()}' added with ID {event_id}."
    
    # Event Management
    def add_event(self, event_data):
        """
        Add an event using a dictionary with keys:
        'Name', 'Description', 'Date', 'Time', 'Capacity'.
        """
        event_id = self._next_event_id
        event = Event(
            event_id,
            event_data.get('name'),
            event_data.get('description'),
            event_data.get('date'),
            event_data.get('time'),
            event_data.get('capacity'),
        )
        self._events[event_id] = event
        self._next_event_id += 1
        print(self._events)
        return f"Event '{event_data.get('name')}' added with ID {event_id}."


    def get_all_events(self):
        for x in self._events.values():
            print(x.get_events())
        if not self._events:
            return "No events available."
        return [event.get_events() for event in self._events.values()]
    
    def get_event_by_id(self,id):
        for x in self._events.values():
            if x.get_event_id() == id:
                return x.get_events_detail()
        return []
    
    def save_data_to_file(self):
        ticket_dict = {ticket.get_ticket_id(): ticket for ticket in self._tickets}
        #self._purchase_history = []
        save_data(self._purchase_history,ticket_dict, self._events, self._users)
