from abc import ABC, abstractmethod


class Order(ABC):
    def __init__(self, client):
        self.client = client
        self.service = ""
        self.status = ""
        self.date = ""
        self.__total_price = 0
        self.appointment_type = ""

    @property
    def total_price(self):
        return self.__total_price

    @total_price.setter
    def total_price(self, price):
        if price < 0:
            raise ValueError("Price can not be less than 0")
        self.__total_price = price

    def update_status(self, status):
        if status not in ["created", "confirmed", "closed"]:
            raise ValueError("Invalid status")
        self.status = status

    @abstractmethod
    def calculate_price(self):
        return self.total_price

    def __str__(self):
        return f"{self.client} | {self.service} | {self.status} | {self.date} | {self.total_price}"


class ConsultationAppointment(Order):

    def __init__(self, client):
        super().__init__(client)
        self.appointment_type = "consultation"
        

    def calculate_price(self):
        self.total_price = 700
        return self.total_price

class ProcedureAppointment(Order):

    def __init__(self, client):
        super().__init__(client)
        self.appointment_type = "procedure"
            

    def calculate_price(self):
        self.total_price = 1000
        return self.total_price

class FollowUpAppointment(Order):

    def __init__(self, client):
        super().__init__(client)
        self.appointment_type = "follow_up"

    def calculate_price(self):
        self.total_price = 500
        return self.total_price