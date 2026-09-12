from datetime import datetime
import re
from abc import ABC, abstractmethod

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

class Order(ABC):
    def __init__(self, client):
        self.client = client
        self.service = ""
        self.status = ""
        self.date = ""
        self.__total_price = 0
        self.appointment_type =""

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


class Service():

    def __init__(self, client):
        self.client = client
        self.service = ""
        self.date = ""
        self.price = 1000

    def __str__(self):
        return f"{self.service} - {self.price}"


            
class ServiceManager:

    def __init__(self):
        self.clients = []
        self.orders = []
        self.client_ord = ""
        self.good = []
        self.services =[]
        self.revenue = 0

    def add_client(self):
        name = input("Input name of the client: ").strip()
        if name == "":
            print("Please enter a name")
            return
        else:
            client = Client(name)
            self.clients.append(client)
            print(f"'{name}' was added")
            return

    def add_order(self):
    
        if len(self.clients) == 0:
            print("No clients in the list, add a client first")
            return
        else:
            print("Clients: ", self.clients)
            client = input("Input name of the client: ").strip()
    
        for c in self.clients:
    
            if c.name == client:

                appointment_type = input("Choose type: consultation, procedure, follow_up: ").strip()


                if appointment_type == "consultation":
                    order = ConsultationAppointment(c)
                elif appointment_type == "procedure":
                    order = ProcedureAppointment(c)
                elif appointment_type == "follow_up":
                    order = FollowUpAppointment(c)
                else:
                    raise ValueError("Invalid appoitment type")

                order.service = input("Choose cosmetics set or etc.: ").strip()
                order.date = datetime.now().strftime("%d.%m.%Y %H:%M")
                status = input("Choose status for order: created, confirmed, closed: ")

                try:
                    order.update_status(status)
                except ValueError as ve:
                    print(f"Celected {ve}")
                    return

                order.calculate_price()
                self.orders.append(order)
                print("Order created: ", order)
                break
        else:
            print("Client name was not found")

    def add_service(self):
        if len(self.clients) == 0:
            print("No clients in the list, add a client first")
            return
        else:
            print("Clients: ", self.clients)
            client = input("Input name of the client: ").strip()

        for c in self.clients:
        
            if c.name == client:
                service = Service(c)
                service.service = input("Choose service wich you prefer: massage, cofee or etc.: ").strip()
                service.date = datetime.now().strftime("%d.%m.%Y %H:%M")
                                                
                try:
                    price = int(input("Input price: "))
                    
                    if price < service.price:
                        raise ValueError("Invalid price")

                    service.price = price

                except ValueError as ve:
                    print(f"Error in {ve}")
                    return
                 
                self.services.append(service)
                print("Service created: ", service)
                break
        else:
            print("Client name was not found")

    def show_orders(self):
        if len(self.orders) == 0:
            print("No orders yet")
            return
        else:
            for i, order in enumerate(self.orders):
                print(f"{i+1}. Appoitment type: {order.appointment_type} |"
                      f"Service: {order.service} |"
                      f"Date: {order.date} |"
                      f"Status: {order.status} |"
                      f"Price: {order.total_price} |")

    def show_services(self):
            if len(self.services) == 0:
                print("No services yet")
                return
            else:
                for i, service in enumerate(self.services):
                    print(f"{i+1}. Client: {service.client} |"
                          f"Service: {service.service} |"
                          f"Date: {service.date} |"
                          f"Price: {service.price} |")

    def calculate_revenue(self):

        self.revenue = 0
        if len(self.orders) == 0:
            print("No orders yet")
            return
        else:
            for order in self.orders:
                self.revenue += order.calculate_price()
            return self.revenue



    def delete_order(self):

        if len(self.orders) == 0:
            print("No orders yet")
            return
        self.show_orders()

        raw = input("Input number to delete order: ")
        
        if not raw.isdigit():
            print("Please enter a number")
            return

        index = int(raw) - 1
        
        if index < 0 or index >= len(self.orders):
            print("Order not found")
            return
        
        deleted_order = self.orders.pop(index)
        print(f"Order - {deleted_order} - deleted")
        return

    def delete_service(self):

        if len(self.services) == 0:
            print("No services yet")
            return
        self.show_services()

        raw = input("Input number to delete service: ")
        
        if not raw.isdigit():
            print("Please enter a number")
            return

        index = int(raw) - 1
        
        if index < 0 or index >= len(self.services):
            print("Service not found")
            return
        
        deleted_service = self.services.pop(index)
        print(f"Order - {deleted_service} - deleted")
        return
        
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






manager = ServiceManager()
       

while True:
    #1.Вивід тексту меню
    print("1. Add client")
    print("2. Create appointment/order")
    print("3. Create service")
    print("4. Show appointments/orders")
    print("5. Show services")
    print("6. Delete order")
    print("7. Delete service")
    print("8. Exit")

    #2. Вибір пункту меню
    
    try:

        choice = int(input("Choose the number of menu: ")) 

    
        if choice == 1:
            manager.add_client()
        elif choice == 2:
            manager.add_order()
        elif choice == 3:
            manager.add_service()
        elif choice == 4:
            manager.show_orders()
        elif choice == 5:
            manager.show_services()
        elif choice == 6:
            manager.delete_order()
        elif choice == 7:
            manager.delete_service()
        elif choice == 8:
            print("Goodbye")
            break
        else:
            print("Unknown option, please select number from 1 to 5 and try again")
    except ValueError as ve:
        print(f"Error in {ve}")
