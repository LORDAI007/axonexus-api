# Axonexus API — Datos en tiempo real (v1)

[![version](https://img.shields.io/github/v/release/LORDAI007/axonexus-api?sort=semver&display_name=tag)](https://github.com/LORDAI007/axonexus-api/releases)
[![license](https://img.shields.io/github/license/LORDAI007/axonexus-api)](https://github.com/LORDAI007/axonexus-api/blob/main/LICENSE)
![status](https://img.shields.io/badge/status-online-brightgreen)
![security](https://img.shields.io/badge/auth-API%20Key-blue)
![server](https://img.shields.io/badge/gateway-Caddy%2BHTTPS-5a5)
![backend](https://img.shields.io/badge/backend-FastAPI%20%2B%20Uvicorn-4a8)

---

API soberana para exponer métricas en tiempo (casi) real, con puerta de enlace HTTPS y autenticación por `X-API-Key`.

**Base URL (prod):** `https://mapa.axonexus.net`  
**Versión:** `v1`  
**Autenticación:** Header `X-API-Key: <tu_api_key>`

---

## Endpoints

### Salud (no requiere clave)

```http
GET /v1/health

## Ejemplos de uso

### 🔹 cURL

```bash
# Verificar salud de la API
curl -X GET "https://mapa.axonexus.net/v1/health"

# Obtener todos los datos (requiere API Key)
curl -H "X-API-Key: TU_API_KEY" -X GET "https://mapa.axonexus.net/v1/datos"

# Obtener datos del río Rímac
curl -H "X-API-Key: TU_API_KEY" -X GET "https://mapa.axonexus.net/v1/datos/rio/Rimac"

# Últimos 5 registros
curl -H "X-API-Key: TU_API_KEY" -X GET "https://mapa.axonexus.net/v1/datos/ultimos?limit=5"

import requests

# Verificar salud
resp = requests.get("https://mapa.axonexus.net/v1/health")
print(resp.json())

# Obtener datos (con API Key)
headers = {"X-API-Key": "TU_API_KEY"}
resp = requests.get("https://mapa.axonexus.net/v1/datos", headers=headers)
print(resp.json())

# Obtener datos del río Rímac
resp = requests.get("https://mapa.axonexus.net/v1/datos/rio/Rimac", headers=headers)
print(resp.json())

# Últimos 5 registros
resp = requests.get("https://mapa.axonexus.net/v1/datos/ultimos?limit=5", headers=headers)
print(resp.json())

