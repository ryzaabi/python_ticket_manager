class Reservation:
    def __init__(self, reservation_id, user_id, visit_date, ticket, status="Confirmed"):
        self._reservation_id = reservation_id
        self._user_id = user_id
        self._visit_date = visit_date
        self._ticket = ticket
        self._status = status

    # Getters and Setters
    def get_reservation_id(self):
        return self._reservation_id

    def get_user_id(self):
        return self._user_id

    def get_visit_date(self):
        return self._visit_date

    def set_visit_date(self, visit_date):
        self._visit_date = visit_date

    def get_ticket(self):
        return self._ticket

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def display_details(self):
        return (
            f"Reservation ID: {self._reservation_id}, User ID: {self._user_id}, "
            f"Visit Date: {self._visit_date}, Ticket: {self._ticket.display_details()}, Status: {self._status}"
        )
