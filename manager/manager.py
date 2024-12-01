
from models.reservation import Reservation
from models.event import Event
class Manager:
    def __init__(self):
        self._users = {}
        self._tickets = []
        self._reservations = {}
        self._events = {}
        self._next_user_id = 1
        self._next_reservation_id = 1
        self._next_event_id = 1

    # User Management
    def add_user(self, user):
        user_id = self._next_user_id
        self._users[user_id] = user
        self._next_user_id += 1
        return f"User '{user.get_name()}' added successfully with ID {user_id}."

    def get_user(self, user_id):
        user = self._users.get(user_id)
        return user.display_details() if user else "User not found."

    def get_all_users(self):
        if not self._users:
            return "No users found."
        return [user.display_details() for user in self._users.values()]

    # Ticket Management
    def add_ticket(self, user, ticket):
        if user.get_user_id() in self._users:
            user.add_ticket(ticket)
            return f"Ticket added for user {user.get_name()}."
        return "User not found."

    def get_user_tickets(self, user):
        if user.get_user_id() in self._users:
            tickets = user.get_purchase_history()
            if tickets:
                return [ticket.display_details() for ticket in tickets]
            return "No tickets found for this user."
        return "User not found."

    # Reservation Management
    def make_reservation(self, user, ticket, visit_date):
        if user.get_user_id() in self._users:
            reservation_id = self._next_reservation_id
            reservation = Reservation(reservation_id, user.get_user_id(), visit_date, ticket)
            self._reservations[reservation_id] = reservation
            self._next_reservation_id += 1
            return f"Reservation {reservation_id} created for user {user.get_name()}."
        return "User not found."

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

    def get_all_events(self):
        if not self._events:
            return "No events available."
        return [event.display_details() for event in self._events.values()]
