import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import settings
from backend.database import sync_engine, Base
from backend.api.router import api_router
from backend.simulation.telemetry_generator import TelemetryGenerator

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB Tables on startup
    Base.metadata.create_all(bind=sync_engine)
    
    # Start background telemetry generator loop
    async def periodic_telemetry():
        while True:
            await asyncio.sleep(settings.SIMULATION_INTERVAL_SECONDS)
            await TelemetryGenerator.run_telemetry_tick()

    task = asyncio.create_task(periodic_telemetry())
    yield
    task.cancel()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

# CORS middleware for React Vite frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {
        "message": "Welcome to VortexNet – Network Monitoring & Management Platform REST API",
        "version": settings.VERSION,
        "docs_url": "/docs"
    }
