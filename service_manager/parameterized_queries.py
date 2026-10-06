import psycopg


DSN = "postgresql://postgres:sergii1983@localhost:5432/aesthetic_medicine"


def parameterized_queries():

    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:

            print("=== PARAMETERIZED QUERIES ===\n")

            # Додаємо тестового клієнта
            cur.execute(
                """
                INSERT INTO clients (name, phone, email)
                VALUES (%s, %s, %s)
                RETURNING id;
                """,
                (
                    "Sava",
                    "+380953701387",
                    "sava@gmail.com"
                )
            )

            client_id = cur.fetchone()[0]

            conn.commit()

            print(f"✅ Створено клієнта ID = {client_id}")

            # Безпечний пошук
            search_name = "Sava"

            cur.execute(
                """
                SELECT *
                FROM clients
                WHERE name = %s;
                """,
                (search_name,)
            )

            result = cur.fetchall()

            print("\n✅ Результат пошуку:")

            for row in result:
                print(row)

            # Демонстрація SQL Injection
            dangerous_input = "'; DROP TABLE clients; --"

            print("\n❌ Небезпечний приклад:")

            print(
                f"SELECT * FROM clients "
                f"WHERE name = '{dangerous_input}'"
            )

            print("\n✅ Безпечний приклад:")

            cur.execute(
                """
                SELECT *
                FROM clients
                WHERE name = %s;
                """,
                (dangerous_input,)
            )

            print(
                "Параметризований запит "
                "не дозволив SQL Injection."
            )


if __name__ == "__main__":
    parameterized_queries()