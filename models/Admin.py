from models.user import User

class Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)

    def view_all_users(self, manager):
        """View details of all users through the Manager."""
        users = manager.get_all_users()
        return "\n".join(users) if users else "No users found."

    def add_event(self, manager, name, description, date, time, capacity):
        """Add an event using the Manager."""
        message = manager.add_event(name, description, date, time, capacity)
        return message

    def view_all_events(self, manager):
        """View all events through the Manager."""
        events = manager.get_all_events()
        return "\n".join(events) if events else "No events available."

    def view_reservations(self, manager):
        """View all reservations through the Manager."""
        reservations = manager.get_all_reservations()
        return "\n".join(reservations) if reservations else "No reservations found."
