# Aesthetic Medicine

def add_client(clients):
    """Додаємо клієнта"""
    name = input("Input name of the client: ").strip()
    if name == "":
        print("Please enter a name")
        return
    else:
        clients.append(name)
        print(f"'{name}' was added")
        return

def add_order(clients, orders):
    """Додаємо замовлення клієнта"""
    if len(clients) == 0:
        print("No clients in the list, add a client first")
        return
    else:
        print("Clients: ", clients)
        client = input("Client name: ").strip()

    if client not in clients:
        print("Client name was not found")
        return
    else:
        good = input("Choose cosmetics set or etc.: ").strip()

    order = {
        "client": client,
        "good": good,
        "status": "Created"
    }

    orders.append(order)
    print("Order created!")


def show_orders(orders):
    """Показуємо замовлення клієнта"""
    if len(orders) == 0:
        print("No orders yet")
        return
    else:
        print("\n--- Orders ---")
        for i, order in enumerate(orders):
            print(f"{i+1}, {order['client']} |"
                  f"{order['good']} | "
                  f"{order['status']}")

def delete_orders(orders):
    """Видалення замовлення"""

    if len(orders) == 0:
        print("No orders in the list")
        return

    show_orders(orders)
    raw = input("Input number to delete order: ")

    if not raw.isdigit():
        print("Please enter a number")
        return

    index = int(raw) - 1

    if index < 0 or index >= len(orders):
        print("Order not found")
        return

    removed = orders.pop(index)
    print(f"Deleted: {removed['client']} — {removed['good']}")


def main():
    """
    1.Вивід тексту меню
    2. Вибір пункту меню
    """
    clients = []
    orders = []

    while True:
        #1.Вивід тексту меню
        print("1. Add client")
        print("2. Create appointment/order")
        print("3. Show appointments/orders")
        print("4. Delete")
        print("5. Exit")

        #2. Вибір пункту меню
        choice = int(input("Choose the number of menu: "))

    
        if choice == 1:
            add_client(clients)
        elif choice == 2:
            add_order(clients, orders)
        elif choice == 3:
            show_orders(orders)
        elif choice == 4:
            delete_orders(orders)
        elif choice == 5:
            print("Goodbye")
            break
        else:
            print("Unknown option, please select number from 1 to 5 and try again")
            



main()

