from .manager import ServiceManager


def run():
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