class Ticket:
    def __init__(self, ticket_id,ticket_type, description, price, validity,discount,limitations):
        self.ticket_id = ticket_id
        self._ticket_type = ticket_type
        self._description = description
        self._price = price
        self._validity = validity
        self._discount = discount
        self._limitations = limitations

    # Getters
    def get_ticket_id(self):
        return self.ticket_id
    
    def get_ticket_type(self):
        return self._ticket_type

    def get_description(self):
        return self._description

    def get_price(self):
        return self._price

    def get_validity(self):
        return self._validity

    def get_discount(self):
        return self._discount
    
    def get_limitations(self):
        return self._limitations

    def display_details(self):
        return [self.ticket_id,self._ticket_type,self._description,self._price,self._validity,self._discount,self._limitations]


class SingleDayTicket(Ticket):
    def __init__(self, price):
        super().__init__(
            ticket_type="Single Day Pass",
            description="Access for one day to all attractions.",
            price=price,
            validity="1 day"
        )


class MultiDayTicket(Ticket):
    def __init__(self, price, days_valid):
        super().__init__(
            ticket_type="Multi-Day Pass",
            description=f"Access for {days_valid} days to all attractions.",
            price=price,
            validity=f"{days_valid} days"
        )