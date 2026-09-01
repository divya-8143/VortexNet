import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "VortexNet – Network Monitoring & Management Platform"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./vortexnet.db")
    SYNC_DATABASE_URL: str = os.getenv("SYNC_DATABASE_URL", "sqlite:///./vortexnet.db")
    
    # JWT Security (Simulated secret for development)
    SECRET_KEY: str = os.getenv("SECRET_KEY", "vortexnet_super_secret_jwt_key_telemetry_monitoring_2026_dev")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    
    # Simulation Config
    SIMULATION_INTERVAL_SECONDS: int = 5
    MAX_SIMULATED_DEVICES: int = 120
    DEFAULT_SNMP_COMMUNITY: str = "public"
    
    class Config:
        case_sensitive = True

settings = Settings()
