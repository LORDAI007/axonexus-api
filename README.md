# Axonexus API — Datos en tiempo real (v1)

![status](https://img.shields.io/badge/status-online-brightgreen)
![security](https://img.shields.io/badge/auth-API%20Key-blue)
![server](https://img.shields.io/badge/gateway-Caddy%20HTTPS-5a5)
![backend](https://img.shields.io/badge/backend-FastAPI%20%2B%20Uvicorn-4a8)

API soberana para exponer métricas en tiempo (casi) real, con puerta de enlace HTTPS y autenticación por `X-API-Key`.

**Base URL (prod):** `https://mapa.axonexus.net`  
**Version:** `v1`  
**Autenticación:** Header `X-API-Key: <tu_api_key>`

---

## Endpoints

### Salud (no requiere clave)
`GET /v1/health`

**200 OK**
```json
{ "ok": true, "msg": "Axonexus API v1 running" }

## 📡 Ejemplos de uso

### 🔹 cURL

**1. Verificar salud de la API**
```bash
curl -X GET https://mapa.axonexus.net/v1/health

**2. Obtener todos los datos (con clave API)**
```bash
curl -H "X-API-Key: <tu_api_key>" \
     -X GET https://mapa.axonexus.net/v1/datos

curl -H "X-API-Key: <tu_api_key>" \
     -X GET "https://mapa.axonexus.net/v1/datos/rio/Rimac"

curl -H "X-API-Key: <tu_api_key>" \
     -X GET "https://mapa.axonexus.net/v1/datos/ultimos?limit=5"

---

✅ Cuando lo pegues, quedará un bloque de ejemplos bien completo.  
Luego hacemos lo mismo con **ejemplos en Python**, ¿quieres que te los prepare también ahora para pegarlos debajo de los cURL?

### 🔹 Python (requests)

**1. Verificar salud de la API**
```python
import requests

resp = requests.get("https://mapa.axonexus.net/v1/health")
print(resp.json())

import requests

headers = {"X-API-Key": "<tu_api_key>"}
resp = requests.get("https://mapa.axonexus.net/v1/datos", headers=headers)
print(resp.json())


import requests

headers = {"X-API-Key": "<tu_api_key>"}
resp = requests.get("https://mapa.axonexus.net/v1/datos/rio/Rimac", headers=headers)
print(resp.json())

import requests

headers = {"X-API-Key": "<tu_api_key>"}
resp = requests.get("https://mapa.axonexus.net/v1/datos/ultimos?limit=5", headers=headers)
print(resp.json())

---

🚀 Con esto, tu README queda “nivel Palantir/GitHub premium”:  
- Badges ✅  
- Endpoints documentados ✅  
- Ejemplos cURL ✅  
- Ejemplos Python ✅  

¿Quieres que te arme también un **diagrama sencillo en ASCII/Markdown** para mostrar cómo fluye:  
`CSV → FastAPI → Endpoint HTTPS → Cliente (cURL / Python)`?

## 🔄 Flujo de Datos

```text
 📄 datos_agua.csv
        │
        ▼
 🚀 FastAPI (main.py)
        │
        ▼
 🌐 Endpoint HTTPS (https://mapa.axonexus.net/v1/*)
        │
   ┌─────┴────────┐
   │              │
   ▼              ▼
 🖥️ Cliente cURL   🐍 Cliente Python (requests)

Esto le da un aire **premium y pedagógico**, como si fuese documentación oficial de Palantir o Stripe.  

👉 ¿Quieres que además preparemos una **sección “Próximos pasos”** en el README (ejemplo: añadir autenticación JWT, métricas en tiempo real, dashboard Plotly)?

## 🚀 Próximos pasos

- 🔑 Autenticación avanzada con JWT (además de API Key).  
- 📊 Métricas en tiempo real (integración con Prometheus/Grafana).  
- 📈 Dashboard interactivo con Plotly/Dash.  
- 🌍 Despliegue multi-región (LatAm, Europa, EAU) para baja latencia.  
- 🤖 Integración con modelos predictivos (IA para pronóstico de caudales y niveles).