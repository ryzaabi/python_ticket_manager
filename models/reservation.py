class Reservation:
    """
    A class to represent a reservation.
    """

    def __init__(self, reservation_id, user_id, visit_date, ticket, status="Confirmed"):
        """
        Initializes a Reservation object with the given details.

        Args:
            reservation_id (str): Unique identifier for the reservation.
            user_id (str): Unique identifier for the user.
            visit_date (str): Date of the visit.
            ticket (Ticket): Associated ticket object.
            status (str, optional): Status of the reservation. Defaults to "Confirmed".
        """
        self._reservation_id = reservation_id
        self._user_id = user_id
        self._visit_date = visit_date
        self._ticket = ticket
        self._status = status

    # Getters and Setters
    def get_reservation_id(self):
        """Gets the reservation ID."""
        return self._reservation_id

    def get_user_id(self):
        """Gets the user ID."""
        return self._user_id

    def get_visit_date(self):
        """Gets the visit date."""
        return self._visit_date

    def set_visit_date(self, visit_date):
        """Sets the visit date."""
        self._visit_date = visit_date

    def get_ticket(self):
        """Gets the associated ticket object."""
        return self._ticket

    def set_ticket(self, ticket):
        """Sets the associated ticket object."""
        self._ticket = ticket

    def get_status(self):
        """Gets the reservation status."""
        return self._status

    def set_status(self, status):
        """
        Sets the reservation status.
        """
        self._status = status

    def display_details(self):
        """
        Displays reservation details.
        """
        return (
            f"Reservation ID: {self._reservation_id}, User ID: {self._user_id}, "
            f"Visit Date: {self._visit_date}, Ticket: {self._ticket.display_details()}, Status: {self._status}"
        )

    def get_summary(self):
        """
        Returns a summary of reservation details.
        """
        return [self._reservation_id, self._user_id, self._visit_date, self._status]

    def cancel_reservation(self):
        """
        Cancels the reservation by changing the status to 'Cancelled'.
        """
        self._status = "Cancelled"
