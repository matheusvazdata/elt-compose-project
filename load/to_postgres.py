import psycopg2
import os
import time

def wait_for_db():
    max_tries = 10
    for i in range(max_tries):
        try:
            conn = psycopg2.connect(
                dbname=os.environ["DB_NAME"],
                user=os.environ["DB_USER"],
                password=os.environ["DB_PASS"],
                host=os.environ["DB_HOST"],
                port=os.environ["DB_PORT"],
            )
            conn.close()
            print("✅ Banco disponível.")
            return
        except psycopg2.OperationalError:
            print(f"⏳ Esperando banco de dados... Tentativa {i+1}/{max_tries}")
            time.sleep(2)
    raise Exception("❌ Não foi possível conectar ao banco após várias tentativas.")

def load_to_db(data):
    wait_for_db()  # <--- aqui é onde espera
    print("🛠️ Carregando dados no PostgreSQL...")

    conn = psycopg2.connect(
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"],
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
    )
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id SERIAL PRIMARY KEY,
            user_id INT,
            title TEXT,
            body TEXT
        );
    """)
    for item in data:
        cur.execute(
            "INSERT INTO posts (user_id, title, body) VALUES (%s, %s, %s)",
            (item["userId"], item["title"], item["body"])
        )
    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ {len(data)} registros inseridos com sucesso!")