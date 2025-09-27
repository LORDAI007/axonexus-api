#!/usr/bin/env python3
import os, json
from pathlib import Path
from datetime import datetime, timezone
from fastapi import FastAPI, Header, HTTPException, Query, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

DATA_DIR = Path(os.environ.get("AX_DATA_DIR", "/srv/axonexus-data"))
API_KEY  = os.environ.get("AX_API_KEY", "")

app = FastAPI(title="Axonexus API", version="1.1.0")

# --- CORS mínimo (ajusta dominios según necesidad)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # pon tu dominio si quieres cerrarlo
    allow_methods=["GET"],
    allow_headers=["*"],
)

def check_key(x_api_key: str|None):
    if API_KEY and (not x_api_key or x_api_key != API_KEY):
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

@app.get("/v1/health")
def v1_health():
    return {"ok": True}

@app.get("/v1/status")
def v1_status(x_api_key: str|None = Header(default=None, alias="X-API-Key")):
    check_key(x_api_key)
    f = DATA_DIR / "status.json"
    if f.exists():
        data = json.loads(f.read_text())
        # age_seconds (salud del ETL)
        try:
            ts = data.get("updated_at")
            if ts:
                # soporta ...Z o con offset
                ts_dt = datetime.fromisoformat(ts.replace("Z","+00:00"))
                data["age_seconds"] = int((datetime.now(timezone.utc) - ts_dt).total_seconds())
        except Exception:
            pass
        return JSONResponse(content=data)
    return JSONResponse(content={"service":"axonexus-api","ok":True,"message":"no status yet"})

@app.get("/v1/metrics/latest")
def v1_metrics_latest(x_api_key: str|None = Header(default=None, alias="X-API-Key")):
    check_key(x_api_key)
    f = DATA_DIR / "latest.json"
    if not f.exists():
        raise HTTPException(status_code=404, detail="No data yet")
    return JSONResponse(content=json.loads(f.read_text()))

@app.get("/v1/metrics/history")
def v1_metrics_history(
    x_api_key: str|None = Header(default=None, alias="X-API-Key"),
    start: str|None = Query(None, description="ISO 8601 (ej. 2025-09-25T00:00:00Z)"),
    end:   str|None = Query(None, description="ISO 8601 (ej. 2025-09-26T00:00:00Z)"),
    limit: int|None = Query(None, ge=1, le=10000, description="Límite de filas"),
):
    check_key(x_api_key)
    import pandas as pd
    pqt = DATA_DIR / "rolling.parquet"
    if not pqt.exists():
        raise HTTPException(status_code=404, detail="No history yet")

    df = pd.read_parquet(pqt)

    # Normalizamos si el DF no tiene 'timestamp' como datetime
    if "timestamp" in df.columns:
        try:
            df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True, errors="coerce")
        except Exception:
            pass

    # Filtros por rango
    if start:
        try:
            start_dt = pd.to_datetime(start, utc=True)
            if "timestamp" in df.columns:
                df = df[df["timestamp"] >= start_dt]
        except Exception:
            pass
    if end:
        try:
            end_dt = pd.to_datetime(end, utc=True)
            if "timestamp" in df.columns:
                df = df[df["timestamp"] <= end_dt]
        except Exception:
            pass

    if limit:
        df = df.sort_values(by="timestamp", ascending=False).head(limit).sort_values(by="timestamp", ascending=True)

    # Serializamos
    return JSONResponse(content=json.loads(df.to_json(orient="records", date_format="iso")))
