import psycopg

DSN = "postgresql://postgres:sergii1983@localhost:5432/aesthetic_medicine"

def create_tables():

    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:

            cur.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(150) NOT NULL,
                    phone VARCHAR(20) NOT NULL,
                    email VARCHAR(100),
                    notes TEXT,
                    created_at TIMESTAMP DEFAULT NOW()
                );
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS services (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(150) NOT NULL,
                    price DECIMAL(10,2) NOT NULL,
                    duration_minutes INTEGER NOT NULL
                );
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    id SERIAL PRIMARY KEY,
                    client_id INTEGER NOT NULL,
                    service_id INTEGER NOT NULL,
                    status VARCHAR(50) NOT NULL,
                    total_price DECIMAL(10, 2) NOT NULL,
                    created_at TIMESTAMP NOT NULL,
                    FOREIGN KEY (client_id)
                    REFERENCES clients(id),
                    FOREIGN KEY (service_id)
                    REFERENCES services(id)
                );
            """)

            cur.execute("""
                CREATE TABLE IF NOT EXISTS inventories (
                id SERIAL PRIMARY KEY,
                name VARCHAR(150) NOT NULL,
                quantity INTEGER NOT NULL,
                price DECIMAL(10, 2) NOT NULL
                );
            """)

            conn.commit()
            print("✅ Таблиця clients, services, orders та inventories створена")

if __name__ == "__main__":
    create_tables()

