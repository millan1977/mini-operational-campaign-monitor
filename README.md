# Mini Operational Campaign Monitor

Proyecto para monitorizar el estado operativo de campañas.

## Setup

### 1. Crear y activar un entorno virtual

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Instalar dependencias

```powershell
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto con:

```text
REQRES_API_KEY=your_api_key
POSTGRES_PASSWORD=your_postgres_password
```

### 4. Preparar PostgreSQL

Con PostgreSQL instalado y en ejecución:

1. Conectarse a la base de datos `postgres`.
2. Ejecutar `sql/create_database.sql`.
3. Conectarse a la nueva base de datos `campaign_monitor`.
4. Ejecutar `sql/schema.sql`.

Esto crea la estructura necesaria:

```text
campaign_monitor
└── public
    └── line_item_snapshots
```

### 5. Ejecutar Campaign Monitor

```powershell
python main.py
```