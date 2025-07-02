import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="task_manager",
        user="TeamKIS",
        password="securepassword",  
        host="localhost",
        port="5432"
    )
