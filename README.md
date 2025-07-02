# Sistema de Gestión de Tareas con PostgreSQL

**Requisitos**
- Python 3.12+
- PostgreSQL 17
- Librerías: `psycopg2-binary`, `uuid`

**Dependencias**:
pip install psycopg2-binary

**Migración de Datos**
Para migrar datos desde tasks.json:
    python migrate.py

**Estructura de la Base de Datos**
    TASKS {
        UUID id PK
        TEXT title
        TEXT description
        VARCHAR(10) status
        TIMESTAMP created_date
    }

**Contacto**
GitHub Repo: https://github.com/Thesergiux/Software-maintenance-administrative-and-technicals-needs.git
Reportar problemas: Abre un issue en el repositorio