import re

class Client:

    def __init__(self, name):
        self.name = name
        self.__phone = ""

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if not re.match(r"^\+380\d{9}$", phone):
            raise ValueError("Invalid phone")
        self.__phone = phone


    def __str__(self):
        return f"{self.name}, {self.__phone}"
    
    def __repr__(self):
        return f"{self.name}, {self.__phone}"