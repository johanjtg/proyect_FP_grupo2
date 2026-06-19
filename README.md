# Expense Tracker API

Rastreador de gastos personales con automatización mediante Gmail + AI by Zapier.

---

## Stack

- **Backend:** Python + FastAPI
- **Base de datos:** SQLite (por defecto) o PostgreSQL
- **Automatización:** Zapier
- **Alertas:** Gmail mediante integración con Zapier

---

## Funcionalidades

### 1. Registro de Gastos (Ingreso Manual)
Registra gastos con monto, categoría, descripción, fecha y tipo (único o suscripción).

**Categorías:** `Food`, `Subscriptions`, `Transport`, `Entertainment`, `Health`, `Other`

### 2. Monitoreo de Suscripciones
Marca cualquier gasto como suscripción recurrente. Las reglas de alerta pueden dispararse cuando el costo supera o cae por debajo de un umbral configurado (ej. `< $100`).

### 3. Resumen por Categoría
Retorna totales agrupados por categoría. Soporta filtros por rango de fechas (semanal / mensual).

### 4. Reglas de Alerta
Configura reglas como:
- `SI categoría = Subscriptions Y monto > $50 → alerta`
- `SI total mensual > $500 → alerta`

Las reglas se almacenan en la base de datos y se evalúan con cada nuevo gasto.

### 5. Automatización con Zapier
El sistema se integra con Gmail y AI by Zapier para procesar automáticamente la información de gastos.
Flujo de trabajo:

```
Nuevo correo en Gmail → AI by Zapier analiza y clasifica → Zapier envía los datos a la API → registro automático del gasto.
```

---

## Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `POST` | `/expenses` | Agregar un gasto |
| `GET` | `/expenses` | Listar gastos (con filtros) |
| `GET` | `/expenses/summary` | Totales agrupados por categoría |
| `POST` | `/alerts/rules` | Crear una regla de alerta |
| `GET` | `/alerts/rules` | Listar reglas de alerta |

Documentación interactiva disponible en `http://localhost:8000/docs` una vez que el servidor esté corriendo.

---

## Estructura del Proyecto

```
Automatization/
├── app/
│   ├── main.py              # Punto de entrada de la app FastAPI
│   ├── database.py          # Conexión y sesión de BD
│   ├── models/
│   │   └── expense.py       # Modelos de BD: Expense + AlertRule
│   ├── schemas/
│   │   └── expense.py       # Schemas Pydantic para requests/responses
│   └── routes/
│       ├── expenses.py      # Endpoints de gastos
│       └── alerts.py        # Endpoints de reglas de alerta
├── requirements.txt
├── .env.example
└── README.md
```

---

## Instalación

```bash
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

---

## Variables de Entorno

| Variable | Descripción | Valor por defecto |
|----------|-------------|-------------------|
| `DATABASE_URL` | Cadena de conexión SQLAlchemy | `sqlite:///./expenses.db` |
| `ZAPIER_WEBHOOK_URL` | URL del webhook de Zapier para automatización | `http://localhost:5678/webhook/expense-alert` |

---

## Implementación Pendiente

Las siguientes funcionalidades están pendientes:

| Archivo | Tarea |
|---------|-------|
| `routes/expenses.py` | `GET /expenses/summary` — totales agrupados por categoría |
| `routes/alerts.py` | `POST /alerts/rules` — guardar regla en BD |
| `routes/alerts.py` | `GET /alerts/rules` — listar reglas desde BD |
| _(nuevo archivo)_ | Motor de automatización → integración con Zapier |
| _(nuevo archivo)_ | Webhook Zapier → HTTP POST a ZAPIER_WEBHOOK_URL` con payload de alerta |
