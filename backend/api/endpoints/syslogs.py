from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_db
from backend.schemas.syslog import SyslogOut, SyslogCreate
from backend.services.syslog_service import SyslogService
from backend.api.deps import get_current_user

router = APIRouter()

@router.get("/", response_model=List[SyslogOut])
async def list_syslogs(
    severity: Optional[str] = None,
    query: Optional[str] = None,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    user = Depends(get_current_user)
):
    return await SyslogService.get_syslogs(db, severity=severity, search_query=query, limit=limit)

@router.post("/", response_model=SyslogOut)
async def ingest_syslog(log_in: SyslogCreate, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    entry = await SyslogService.ingest_log(db, log_in)
    return SyslogOut.model_validate(entry)
