from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_db
from backend.schemas.audit import AuditLogOut
from backend.services.audit_service import AuditService
from backend.api.deps import get_current_user

router = APIRouter()

@router.get("/", response_model=List[AuditLogOut])
async def list_audit_logs(username: Optional[str] = None, limit: int = 100, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    return await AuditService.get_audit_logs(db, username=username, limit=limit)
