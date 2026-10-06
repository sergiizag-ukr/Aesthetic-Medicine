import psycopg


DSN = "postgresql://postgres:sergii1983@localhost:5432/aesthetic_medicine"


def create_client(name, phone, email):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO clients (name, phone, email)
                VALUES (%s, %s, %s)
                RETURNING id;
                """,
                (name, phone, email)
            )

            client_id = cur.fetchone()[0]

            conn.commit()

            return client_id


def read_client(client_id):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT *
                FROM clients
                WHERE id = %s;
                """,
                (client_id,)
            )

            return cur.fetchone()


def update_client(client_id, email):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE clients
                SET email = %s
                WHERE id = %s;
                """,
                (email, client_id)
            )

            conn.commit()


def delete_client(client_id):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM clients
                WHERE id = %s;
                """,
                (client_id,)
            )

            conn.commit()


if __name__ == "__main__":

    # CREATE
    client_id = create_client(
        "Sava",
        "+380953701387",
        "sava@gmail.com"
    )

    print(f"CREATE -> ID = {client_id}")

    # READ
    print("READ ->", read_client(client_id))

    # UPDATE
    update_client(
        client_id,
        "new_email@gmail.com"
    )

    print("UPDATE ->", read_client(client_id))

    # DELETE
    delete_client(client_id)

    print("DELETE ->", read_client(client_id))