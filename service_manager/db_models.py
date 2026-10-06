from database import get_connection
from datetime import datetime


def bd_add_client(name, phone, email):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO clients (
                    name,
                    phone,
                    email
                )
                VALUES (%s, %s, %s)
                RETURNING id;
                """,
                (name, phone, email)
            )

            client_id = cur.fetchone()[0]

            conn.commit()

            return client_id


def get_all_clients():

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                SELECT
                    id,
                    name,
                    phone,
                    email
                FROM clients
                ORDER BY name;
            """)

            rows = cur.fetchall()

            return [
                {
                    "id": row[0],
                    "name": row[1],
                    "phone": row[2],
                    "email": row[3]
                }
                for row in rows
            ]


def bd_add_service(name, price, duration):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO services (
                    name,
                    price,
                    duration_minutes
                )
                VALUES (%s, %s, %s)
                RETURNING id;
                """,
                (name, price, duration)
            )

            service_id = cur.fetchone()[0]

            conn.commit()

            return service_id


def get_all_services():

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                SELECT
                    id,
                    name,
                    duration_minutes,
                    price
                FROM services
                ORDER BY name;
            """)

            rows = cur.fetchall()

            return [
                {
                    "id": row[0],
                    "name": row[1],
                    "duration": row[2],
                    "price": row[3]
                }
                for row in rows
            ]


def bd_add_order(client_id, service_id):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT price
                FROM services
                WHERE id = %s;
                """,
                (service_id,)
            )

            service = cur.fetchone()

            if service is None:
                raise ValueError("Service not found")

            total_price = service[0]

            cur.execute(
                """
                INSERT INTO orders (
                    client_id,
                    service_id,
                    status,
                    total_price,
                    created_at
                )
                VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
                RETURNING id;
                """,
                (
                    client_id,
                    service_id,
                    "Created",
                    total_price,
                    datetime.now()
                )
            )

            order_id = cur.fetchone()[0]

            conn.commit()

            return order_id


def get_all_orders():

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                SELECT *
                FROM orders
                ORDER BY client_id;
            """)

            return cur.fetchall()


def get_orders_with_details():

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("""
                SELECT
                    orders.id,
                    clients.name,
                    services.name,
                    orders.total_price,
                    orders.created_at,
                    orders.status
                FROM orders
                INNER JOIN clients
                    ON orders.client_id = clients.id
                INNER JOIN services
                    ON orders.service_id = services.id
                ORDER BY orders.id;
            """)

            rows = cur.fetchall()

            return [
                {
                    "id": row[0],
                    "client_name": row[1],
                    "service_name": row[2],
                    "total_price": row[3],
                    "created_at": row[4],
                    "status": row[5]
                }
                for row in rows
            ]


def update_order_status(order_id, new_status):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                UPDATE orders
                SET status = %s
                WHERE id = %s;
                """,
                (new_status, order_id)
            )

            conn.commit()

            return cur.rowcount > 0


def add_inventory_item(name, quantity, price):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                INSERT INTO inventories (
                    name,
                    quantity,
                    price
                )
                VALUES (%s, %s, %s)
                RETURNING id;
                """,
                (name, quantity, price)
            )

            inventory_id = cur.fetchone()[0]

            conn.commit()

            return inventory_id


def get_low_stock_items(threshold):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                SELECT *
                FROM inventories
                WHERE quantity < %s;
                """,
                (threshold,)
            )

            rows = cur.fetchall()

            return [
                {
                    "id": row[0],
                    "name": row[1],
                    "quantity": row[2],
                    "price": row[3]
                }
                for row in rows
            ]


def bd_delete_order(order_id):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                DELETE FROM orders
                WHERE id = %s;
                """,
                (order_id,)
            )

            conn.commit()

            return cur.rowcount > 0


def bd_delete_service(service_id):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                DELETE FROM services
                WHERE id = %s;
                """,
                (service_id,)
            )

            conn.commit()

            return cur.rowcount > 0