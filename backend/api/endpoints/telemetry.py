from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_db
from backend.schemas.telemetry import BandwidthSummary, SlaProbeOut
from backend.services.telemetry_service import TelemetryService
from backend.api.deps import get_current_user

router = APIRouter()

@router.get("/bandwidth/summary", response_model=BandwidthSummary)
async def get_bandwidth_summary(db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    return await TelemetryService.get_bandwidth_summary(db)

@router.get("/sla/probes", response_model=List[SlaProbeOut])
async def get_sla_probes(db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    return await TelemetryService.get_sla_probes(db)
