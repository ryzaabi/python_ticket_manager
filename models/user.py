class User:
    """
    Represents a user with basic attributes.
    """
    def __init__(self, user_id, name, email, password):
        """
        Initializes a User object.

        Args:
            user_id (str): Unique identifier for the user.
            name (str): Name of the user.
            email (str): Email address of the user.
            password (str): Password for the user account.
        """
        self._user_id = user_id
        self._name = name
        self._email = email
        self._password = password

    # Getters
    def get_user_id(self):
        """Returns the user's unique ID."""
        return self._user_id

    def get_name(self):
        """Returns the user's name."""
        return self._name

    def get_email(self):
        """Returns the user's email address."""
        return self._email

    def get_password(self):
        """Returns the user's password."""
        return self._password

    # Setters
    def set_name(self, name):
        """Updates the user's name."""
        self._name = name

    def set_email(self, email):
        """Updates the user's email address."""
        self._email = email

    def set_password(self, password):
        """Updates the user's password."""
        self._password = password

    def display_details(self):
        """
        Returns the user's details as a list (excluding sensitive data).
        """
        return [self._user_id, self._name, self._email]
