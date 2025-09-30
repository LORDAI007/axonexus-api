# 🌊 Axonexus Water API (v1)

API de ejemplo para consultar **datos de agua en ríos peruanos** (caudal, nivel, temperatura) a partir de un CSV, usando [FastAPI](https://fastapi.tiangolo.com/).

---

## 🚀 Endpoints base
Prefijo: `/v1/*`

- `GET /` → Información general de la API  
- `GET /datos` → Obtener todos los datos (con filtros opcionales)  
- `GET /datos/rio/{nombre}` → Filtrar por río  
- `GET /datos/estadisticas` → Estadísticas (promedio, mínimo, máximo, mediana)  
- `GET /rios` → Lista de ríos disponibles  
- `GET /estaciones` → Lista de estaciones  
- `GET /datos/ultimos` → Últimos N registros  

---

## ▶️ Ejecutar en local

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar API
uvicorn water.main:app --host 0.0.0.0 --port 9000 --reload