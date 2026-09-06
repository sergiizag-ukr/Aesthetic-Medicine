from datetime import datetime

from .models import (
    Client,
    ConsultationAppointment,
    ProcedureAppointment,
    FollowUpAppointment,
    Service,
)

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