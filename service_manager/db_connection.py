import psycopg

DSN = "postgresql://postgres:sergii1983@localhost:5432/aesthetic_medicine"

try:
    with psycopg.connect(DSN) as conn:
        print("✅ Успішно підключені до PostgreSQL!")

        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            version = cur.fetchone()[0]
            print(version)

except psycopg.Error as e:
    print(f"❌ Помилка: {e}")