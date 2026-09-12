import re

class Client:

    def __init__(self, name):
        self.name = name
        self.__phone = ""
        self.__email = ""

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not re.match(r"^\+380\d{9}$", phone):
            raise ValueError("Invalid phone")
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if not re.match(r"^[a-zA-Z0-9._%]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            raise ValueError("Invalid email")
        self.__email = email


    def __str__(self):
        return f"{self.name}, {self.__phone}, {self.__email}"
    
    def __repr__(self):
        return f"{self.name}, {self.__phone}, {self.__email}"