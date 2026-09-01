from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_db
from backend.schemas.alert import AlertRuleOut, AlertRuleCreate
from backend.schemas.incident import IncidentOut, IncidentCreate, IncidentUpdate
from backend.services.alert_service import AlertService
from backend.services.incident_service import IncidentService
from backend.api.deps import get_current_user

router = APIRouter()

@router.get("/rules", response_model=List[AlertRuleOut])
async def list_rules(db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    rules = await AlertService.get_all_rules(db)
    return [AlertRuleOut.model_validate(r) for r in rules]

@router.post("/rules", response_model=AlertRuleOut)
async def create_rule(rule_in: AlertRuleCreate, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    rule = await AlertService.create_rule(db, rule_in)
    return AlertRuleOut.model_validate(rule)

@router.get("/incidents", response_model=List[IncidentOut])
async def list_incidents(status: Optional[str] = None, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    incidents = await IncidentService.get_all_incidents(db, status_filter=status)
    return [IncidentOut.model_validate(i) for i in incidents]

@router.post("/incidents", response_model=IncidentOut)
async def create_incident(inc_in: IncidentCreate, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    inc = await IncidentService.create_incident(db, inc_in)
    return IncidentOut.model_validate(inc)

@router.put("/incidents/{incident_id}", response_model=IncidentOut)
async def update_incident(incident_id: int, inc_in: IncidentUpdate, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    inc = await IncidentService.update_incident(db, incident_id, inc_in)
    return IncidentOut.model_validate(inc)
