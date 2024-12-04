class Event:
    """
    A class to represent an event.

    Attributes:
        event_id (str): Unique identifier for the event.
        name (str): Name of the event.
        description (str): Description of the event.
        date (str): Date of the event (format: YYYY-MM-DD).
        time (str): Time of the event (format: HH:MM).
        capacity (int): Maximum number of attendees.
        reservations (list): List of reservations for the event.
    """

    def __init__(self, event_id, name, description, date, time, capacity):
        """
        Initializes an Event object with the given details.

        Args:
            event_id (str): Unique identifier for the event.
            name (str): Name of the event.
            description (str): Description of the event.
            date (str): Date of the event.
            time (str): Time of the event.
            capacity (int): Maximum number of attendees.
        """
        self._event_id = event_id
        self._name = name
        self._description = description
        self._date = date
        self._time = time
        self._capacity = capacity
        

    # Getters and Setters
    def get_event_id(self):
        """Gets the event ID."""
        return self._event_id

    def get_name(self):
        """Gets the event name."""
        return self._name

    def set_name(self, name):
        """Sets the event name."""
        self._name = name

    def get_description(self):
        """Gets the event description."""
        return self._description

    def set_description(self, description):
        """Sets the event description."""
        self._description = description

    def get_date(self):
        """Gets the event date."""
        return self._date

    def set_date(self, date):
        """Sets the event date."""
        self._date = date

    def get_time(self):
        """Gets the event time."""
        return self._time

    def set_time(self, time):
        """Sets the event time."""
        self._time = time

    def get_capacity(self):
        """Gets the event capacity."""
        return self._capacity

    def set_capacity(self, capacity):
        """Sets the event capacity."""
        self._capacity = capacity

    def display_details(self):
        """
        Displays event details with remaining capacity.

        Returns:
            str: Formatted string of event details.
        """
        remaining_capacity = self._capacity - len(self._reservations)
        return (
            f"Event ID: {self._event_id}, Name: {self._name}, Description: {self._description}, "
            f"Date: {self._date}, Time: {self._time}, Capacity: {remaining_capacity} remaining"
        )

    def get_events(self):
        """
        Returns a summary of event details.

        Returns:
            list: Summary of event details as a list.
        """
        remaining_capacity = self._capacity - len(self._reservations)
        return [self._event_id, self._name, self._description, self._date, self._time, remaining_capacity]

    def get_events_detail(self):
        """
        Returns detailed event information.

        Returns:
            list: Detailed event information as a list.
        """
        return [self._name, self._description, self._date, self._time]
