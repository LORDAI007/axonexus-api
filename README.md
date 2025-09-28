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
