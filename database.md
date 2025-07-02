# Esquema de Base de Datos PostgreSQL

## Tabla: tasks
```sql
CREATE TABLE tasks (
    id UUID PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    status VARCHAR(10) CHECK (status IN ('Pending', 'Completed')),
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Ventajas del Diseño
- Integridad de datos mediante restricciones SQL
- Mayor escalabilidad que JSON
- Compatible con herramientas profesionales como SQLAlchemy y dashboards
- Preparado para ampliaciones futuras (usuarios, historial, prioridades)