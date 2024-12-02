import pickle
import os
from models.user import User
from models.ticket import Ticket
from models.event import Event

# Mock Data for Tickets
tickets = {
    1: Ticket(1, "Single-Day Pass", "Access to the park for one day", "275 DHS", "1 Day", "None", "Valid only on selected date"),
    2: Ticket(2, "Two-Day Pass", "Access to the park for two consecutive days", "480 DHS", "2 Days", "10% online discount", "Cannot split over multiple trips"),
    3: Ticket(3, "Family Pass", "Access for a family of four", "900 DHS", "1 Day", "5% discount for families", "Valid only on weekends"),
    4: Ticket(4, "Annual Pass", "Unlimited access for one year", "2500 DHS", "365 Days", "15% discount on renewal", "Non-transferable"),
    5: Ticket(5, "VIP Pass", "Priority access and exclusive perks", "1500 DHS", "1 Day", "None", "Includes only one VIP area access"),
}

# Creating a dictionary of events with event_id as the key
events = {
    1: Event(1, "Music Festival", "An amazing music event", "2024-12-10", "6:00 PM", 500),
    2: Event(2, "Food Carnival", "Delicious cuisines from around the world", "2024-12-15", "12:00 PM", 300),
    3: Event(3, "Art Exhibition", "A showcase of local talent", "2024-12-20", "10:00 AM", 200),
    4: Event(4, "Technology Expo", "Explore the latest tech innovations", "2024-12-25", "9:00 AM", 400),
    5: Event(5, "Comedy Night", "A night of laughter and fun", "2024-12-30", "8:00 PM", 350),
}
# Mock Data for Users
users = {
    1: User(1, "Alice Johnson", "alice.johnson@example.com", "password123"),
    2: User(2, "Bob Smith", "bob.smith@example.com", "securepass456"),
    3: User(3, "Charlie Davis", "charlie.davis@example.com", "mypassword789"),
    4: User(4, "Diana Lee", "diana.lee@example.com", "strongpass321"),
    5: User(5, "admin", "ethan.brown@example.com", "admin"),
}


@staticmethod
def load_or_create_data(pickle_file="data.pkl"):
    """
    Check if the pickle file exists. If it does, load and return the arrays from it.
    Otherwise, use mock data and save it to the pickle file.
    
    :param pickle_file: Name of the pickle file to check or create.
    :return: Tuple of (tickets, events, users).
    """
    if os.path.exists(pickle_file):
        print("Pickle file found. Loading data...")
        with open(pickle_file, "rb") as file:
            data = pickle.load(file)
            return data.get("tickets", []), data.get("events", []), data.get("users", [])
    else:
        print("No pickle file found. Using mock data and saving it to a pickle file...")
        # Save mock data to the pickle file
        data = {"tickets": tickets, "events": events, "users": users}
        with open(pickle_file, "wb") as file:
            pickle.dump(data, file)
        return tickets, events, users
    
@staticmethod
def save_data(tickets, events, users, pickle_file="data.pkl"):
    """
    Save the given data back to the pickle file.

    :param tickets: The list of tickets to be saved.
    :param events: The list of events to be saved.
    :param users: The list of users to be saved.
    :param pickle_file: The name of the pickle file where data will be saved.
    """
    data = {"tickets": tickets, "events": events, "users": users}
    with open(pickle_file, "wb") as file:
        pickle.dump(data, file)
    print("Data saved successfully to pickle file.")
