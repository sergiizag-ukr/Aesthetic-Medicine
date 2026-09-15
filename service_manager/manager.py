from .models import Client
from .decorators import log_action, validate_price
from .db_models import (
    bd_add_client,
    bd_add_order,
    bd_add_service,
    get_all_clients,
    get_all_services,
    get_orders_with_details,
    add_inventory_item,
    get_low_stock_items,
    bd_delete_order,
    bd_delete_service
    )




class ServiceManager:

    def __init__(self):
        self.clients_ord = ""
        self.good = []
        self.revenue = 0
    

    @log_action
    def add_client(self):
        name = input("Input name of the client: ").strip()
        if name == "":
            print("Please enter a name")
            return

        phone = input("Input phone: ").strip()
        if phone == "":
            print("Please enter a phone")
            return

        client = Client(name)
        
        try:
            client.phone = phone
        except ValueError as ve:
            print(f"Error: {ve}")
            return

        email = input("Input email: ").strip()

        try:
            client.email = email
        except ValueError as ve:
            print(f"Error: {ve}")
            return

        client_id = bd_add_client(client.name, client.phone, client.email)

        print(f"Client added. ID: {client_id}")
        return client_id
    
    @log_action
    def add_order(self):

        clients = get_all_clients()
        if not clients:
            print("No clients found")
            return
        
        for client in clients:
            print(client["id"], client["name"], client["phone"])

        client_id = int(input("Input client ID: "))

        services = get_all_services()
        if not services:
            print("No services found")
            return

        for service in services:
            print(service["id"], service["name"], service["duration"], service["price"])
        
        service_id = int(input("Input service ID: "))

        order_id = bd_add_order(client_id, service_id)

        print(f"Order created. ID: {order_id}")
    
    def add_service(self):
        name = input("Input the name of service: ").strip()
        if name == "":
            print("Please enter a service name")
            return

        try:
            price = int(input("Input the price service: "))
        except ValueError as ve:
            print(f"Error: {ve}")
            return

        try:
            duration = int(input("Input duration in minutes: "))
        except ValueError as ve:
            print(f"Error: {ve}")
            return

        self.create_service(name, price, duration)
    
    @log_action
    @validate_price
    def create_service(self, name, price, duration):
        service_id = bd_add_service(name, price, duration)
        print(f"Service added. ID: {service_id}")
        return service_id
        

    @log_action
    def show_orders(self):
        orders = get_orders_with_details()

        if not orders:
            print("No orders found")
            return

        for order in orders:
            print(f"{order['id']}, {order['client_name']}, {order['service_name']}, {order['total_price']}, {order['created_at']}, {order['status']}")

        return
    
    @log_action
    def show_services(self):
        services = get_all_services()

        if not services:
            print("No services found")
            return

        for service in services:
            print(f"{service['id']}. {service['name']}. {service['duration']}. {service['price']}")
        return
    @log_action
    def add_inventory(self):

        name = input("Input inventory name of the inventory: ")
        if name == "":
            print("Please enter the name of inventory")
            return

        try:
            quantity = int(input("Enter the quantity: "))
        except ValueError as ve:
            print(f"Error: {ve}")
            return

        try:
            price = int(input("Enter the price: "))
        except ValueError as ve:
            print(f"Error: {ve}")
            return

        inventory_id = add_inventory_item(name, quantity, price)
        print(f"Inventory added. ID: {inventory_id}")
        return


    def show_low_stock(self):

        try:
            threshold = int(input("Enter the threshold for invenrories: "))
        except ValueError as ve:
            print(f"Error: {ve}")
            return

        stock = get_low_stock_items(threshold)

        if not stock:
            print("No stock found")
            return

        for item in stock:
            print(f"{item['id']}, {item['name']}, {item['quantity']}, {item['price']}")

        return


   

    # def calculate_revenue(self):

    #     self.revenue = 0
    #     if len(self.orders) == 0:
    #         print("No orders yet")
    #         return
    #     else:
    #         for order in self.orders:
    #             self.revenue += order.calculate_price()
    #         return self.revenue


    @log_action
    def delete_order(self):

        orders = get_orders_with_details()
        
        if not orders:
            print("No orders found")
            return
        
        for order in orders:
            print(f"{order['id']}, {order['client_name']}, {order['service_name']}, {order['total_price']}, {order['created_at']}, {order['status']}")

        order_id = int(input("Chosse order ID to delete the order: "))

        order_del = bd_delete_order(order_id)

        if order_del:
            print("Order deleted")
        else:
            print("Order not found")

       

    @log_action       
    def delete_service(self):
        services = get_all_services()

        if not services:
            print("No services found")
            return

        for service in services:
            print(
                f"{service['id']}, "
                f"{service['name']}, "
                f"{service['duration']}, "
                f"{service['price']}"
            )

        service_id = int(input("Choose service ID to delete: "))
        service_del = bd_delete_service(service_id)
        if service_del:
            print("Service deleted")
        else:
            print("Service not found")
        return