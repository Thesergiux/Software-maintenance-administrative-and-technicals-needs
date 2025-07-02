# Guía de Instalación y Configuración

## Requisitos
- PostgreSQL versión 17 o superior
- Python 3.10 o superior
- Biblioteca psycopg2 (`pip install psycopg2`)

## Instalación de PostgreSQL
1. Descargar desde: https://www.postgresql.org/download/
2. Crear base de datos:
```
CREATE DATABASE task_manager;
CREATE USER TeamKIS WITH PASSWORD 'securepassword';
GRANT ALL PRIVILEGES ON DATABASE task_manager TO TeamKIS;
```

## Configuración de conexión
Modificar `db.py` con los parámetros correctos de tu entorno:

```python
psycopg2.connect(
    dbname="task_manager",
    user="TeamKIS",
    password="securepassword",
    host="localhost",
    port="5432"
)
```