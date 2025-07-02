import json
import uuid
from db import get_connection

def migrate_json_to_postgres(json_path="../tasks.json"):
    with open(json_path, "r", encoding="utf-8") as file:
        tasks = json.load(file)

    conn = get_connection()
    cur = conn.cursor()

    for task in tasks:
        cur.execute("""
            INSERT INTO tasks (id, title, description, status, created_date)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            uuid.UUID(task["id"]),
            task["title"],
            task["description"],
            task["status"],
            task["created_date"]
        ))

    conn.commit()
    cur.close()
    conn.close()
    print(" Migracion completada.")

if __name__ == "__main__":
    migrate_json_to_postgres()
