class Event:
    def __init__(self, event_id, name, description, date, time, capacity):
        self._event_id = event_id
        self._name = name
        self._description = description
        self._date = date
        self._time = time
        self._capacity = capacity
        self._reservations = []

    # Getters and Setters
    def get_event_id(self):
        return self._event_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_capacity(self):
        return self._capacity

    def add_reservation(self, reservation):
        if len(self._reservations) < self._capacity:
            self._reservations.append(reservation)
            return f"Reservation added for event {self._name}."
        return "Event capacity reached."

    def display_details(self):
        remv =  int(self._capacity) - len(self._reservations)
        return (
            f"Event ID: {self._event_id}, Name: {self._name}, Description: {self._description}, "
            f"Date: {self._date}, Time: {self._time}, Capacity: {remv} remaining"
        )
