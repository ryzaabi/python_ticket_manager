class User:
    def __init__(self, user_id, name, email, password):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._password = password
        

    # Getters and Setters
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_email(self):
        return self._email
    
    def get_password(self):
        return self._password

    def set_email(self, email):
        self._email = email

    def display_details(self):
        return [self._user_id, self._name,self._email, self.get_password()]
