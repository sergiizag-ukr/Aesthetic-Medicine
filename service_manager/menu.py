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
        print("6. Add inventory")
        print("7. Show low stock")
        print("8. Delete order")
        print("9. Delete service")
        print("10. Exit")

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
                manager.add_inventory()
            elif choice == 7:
                manager.show_low_stock()
            elif choice == 8:
                manager.delete_order()
            elif choice == 9:
                manager.delete_service()
            elif choice == 10:
                print("Goodbye")
                break
            else:
                print("Unknown option, please select number from 1 to 10 and try again")
        except ValueError as ve:
            print(f"Error in {ve}")