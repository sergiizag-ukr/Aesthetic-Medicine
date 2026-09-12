from database import get_connection
from datetime import datetime

def bd_add_client(name, phone, email):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO clients (name, phone, email) VALUES (?, ?, ?)",
            (name, phone, email)
        )
        conn.commit()
        return cursor.lastrowid


def get_all_clients():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clients ORDER BY name")
        return cursor.fetchall()

def bd_add_service(name, price, duration):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO services (name, price, duration) VALUES (?, ?, ?)",
            (name, price, duration)
        )
        conn.commit()
        return cursor.lastrowid

def bd_add_order(client_id, service_id):

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT price FROM services WHERE id = ?",
            (service_id,)
        )

        service = cursor.fetchone()

        if service is None:
            raise ValueError("Service not found")
        
        total_price = service["price"]

        status = "Created"
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        

        cursor.execute("INSERT INTO orders (client_id, service_id, status, total_price, created_at) VALUES (?, ?, ?, ?, ?)",
                       (client_id, service_id, status, total_price, created_at)
        )
        conn.commit()
        return cursor.lastrowid

def get_all_services():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM services ORDER BY name")
        return cursor.fetchall()

def get_all_orders():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders ORDER by client_id")
        return cursor.fetchall()

def get_orders_with_details():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT
        orders.id,
        clients.name AS client_name,
        services.name AS service_name,
        orders.total_price,
        orders.created_at,
        orders.status
        FROM orders
        INNER JOIN clients ON orders.client_id = clients.id
        INNER JOIN services ON orders.service_id = services.id""")
        return cursor.fetchall()


def  update_order_status(order_id, new_status):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE orders SET status = ? WHERE id = ?",
            (new_status, order_id)
        )
        if cursor.rowcount == 0:
            return False
        
        conn.commit()

        return True

def add_inventory_item(name, quantity, price):
    with get_connection() as conn:
        cursor = conn.cursor()
    
        cursor.execute("INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)",
            (name, quantity, price)
        )
        conn.commit()
        return cursor.lastrowid

def get_low_stock_items(threshold):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM inventory WHERE quantity < ?",
            (threshold,)
        )
        return cursor.fetchall()

def bd_delete_order(order_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM orders WHERE id = ?",
            (order_id,)
        )

        if cursor.rowcount == 0:
            return False
        conn.commit()
        return True

def bd_delete_service(service_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM services WHERE id = ?",
            (service_id,)
        )
        if cursor.rowcount == 0:
            return False
        conn.commit()
        return True


