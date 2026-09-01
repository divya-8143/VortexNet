from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_db
from backend.schemas.traffic import TopTalkerItem, ProtocolDistributionItem, NetFlowRecordOut
from backend.services.traffic_service import TrafficService
from backend.api.deps import get_current_user

router = APIRouter()

@router.get("/top-talkers", response_model=List[TopTalkerItem])
async def get_top_talkers(db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    return await TrafficService.get_top_talkers(db)

@router.get("/protocols", response_model=List[ProtocolDistributionItem])
async def get_protocols(db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    return await TrafficService.get_protocol_distribution(db)

@router.get("/flows", response_model=List[NetFlowRecordOut])
async def get_flows(db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    return await TrafficService.get_recent_flows(db)
