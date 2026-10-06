import psycopg


DSN = "postgresql://postgres:sergii1983@localhost:5432/aesthetic_medicine"


def demonstrate_transactions():

    print("=== TRANSACTIONS ===\n")

    # Успішна транзакція
    try:
        with psycopg.connect(DSN) as conn:
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
                    (
                        "Anna",
                        "+380501234567",
                        "anna@gmail.com"
                    )
                )

                client_id = cur.fetchone()[0]

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
                        "Lip Filler",
                        4000,
                        60
                    )
                )

                service_id = cur.fetchone()[0]

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
                        NOW()
                    )
                    """,
                    (
                        client_id,
                        service_id,
                        "Created",
                        4000
                    )
                )

                conn.commit()

                print("✅ Успішна транзакція виконана")

    except psycopg.Error as e:
        print(f"❌ Помилка: {e}")

    print("\n========================\n")

    # Транзакція з ROLLBACK
    try:
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:

                try:

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
                        (
                            "Test User",
                            "+380999999999",
                            "test@gmail.com"
                        )
                    )

                    print("Клієнт створений")

                    # Спеціально викликаємо помилку
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
                            NOW()
                        )
                        """,
                        (
                            9999,
                            9999,
                            "Created",
                            5000
                        )
                    )

                    conn.commit()

                except Exception as e:

                    conn.rollback()

                    print("❌ Помилка транзакції")
                    print("✅ Виконано ROLLBACK")
                    print(e)

    except psycopg.Error as e:
        print(e)


if __name__ == "__main__":
    demonstrate_transactions()