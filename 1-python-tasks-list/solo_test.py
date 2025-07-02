import psycopg2

try:
    conn = psycopg2.connect(
        dbname="task_manager",
        user="TeamKIS",
        password="TeamKIS2025",
        host="localhost",
        port="5432"
    )
    print("Conectado con éxito")

    cur = conn.cursor()
    cur.execute("SELECT version();")
    print(cur.fetchone())

    cur.close()
    conn.close()

except Exception as e:
    print(f"Error de conexión: {e}")
