from fastapi import APIRouter
from backend.api.endpoints import auth, devices, ipam, topology, telemetry, traffic, alerts, syslogs, audit, reports

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(devices.router, prefix="/devices", tags=["Device Management"])
api_router.include_router(ipam.router, prefix="/ipam", tags=["IP Address Management"])
api_router.include_router(topology.router, prefix="/topology", tags=["Network Topology"])
api_router.include_router(telemetry.router, prefix="/telemetry", tags=["Telemetry & SLA"])
api_router.include_router(traffic.router, prefix="/traffic", tags=["Traffic & NetFlow Analytics"])
api_router.include_router(alerts.router, prefix="/alerts", tags=["Alerts & Incident Management"])
api_router.include_router(syslogs.router, prefix="/syslogs", tags=["Network Syslogs"])
api_router.include_router(audit.router, prefix="/audit", tags=["Audit Trail"])
api_router.include_router(reports.router, prefix="/reports", tags=["Executive Reports"])
