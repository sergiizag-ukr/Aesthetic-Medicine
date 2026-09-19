import re
from dataclasses import dataclass

@dataclass
class Client:
    name: str
    phone: str
    email: str = ""
    notes: str = ""

    def __post_init__(self):
        if not re.match(r"^\+380\d{9}$", self.phone):
            raise ValueError("Invalid phone")

        if self.email and not re.match(r"^[a-zA-Z0-9._%]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", self.email):
            raise ValueError("Invalid email")

    def display(self):
        return f"{self.name} | {self.phone}"

