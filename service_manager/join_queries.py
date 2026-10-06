import psycopg


DSN = "postgresql://postgres:sergii1983@localhost:5432/aesthetic_medicine"


def join_queries():

    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:

            # Додаємо сервіс
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
                (
                    "Botox",
                    5000,
                    60
                )
            )

            service_id = cur.fetchone()[0]

            # Додаємо замовлення
            cur.execute(
                """
                INSERT INTO orders (
                    client_id,
                    service_id,
                    status,
                    total_price,
                    created_at
                )
                VALUES (%s, %s, %s, %s, NOW())
                RETURNING id;
                """,
                (
                    1,
                    service_id,
                    "Created",
                    5000
                )
            )

            order_id = cur.fetchone()[0]

            conn.commit()

            print(f"Service ID: {service_id}")
            print(f"Order ID: {order_id}")

            cur.execute(
                """
                SELECT
                    o.id,
                    c.name,
                    s.name,
                    o.total_price,
                    o.status,
                    o.created_at
                FROM orders o
                INNER JOIN clients c
                    ON o.client_id = c.id
                INNER JOIN services s
                    ON o.service_id = s.id
                ORDER BY o.id;
                """
            )

            rows = cur.fetchall()

            print("\n=== JOIN QUERIES ===\n")

            for row in rows:
                print(
                    f"Order ID: {row[0]} | "
                    f"Client: {row[1]} | "
                    f"Service: {row[2]} | "
                    f"Price: {row[3]} | "
                    f"Status: {row[4]} | "
                    f"Created: {row[5]}"
                )


if __name__ == "__main__":
    join_queries()