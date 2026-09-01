from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.audit import AuditLog
from backend.schemas.audit import AuditLogCreate, AuditLogOut

class AuditService:
    @staticmethod
    async def log_action(db: AsyncSession, log_in: AuditLogCreate) -> AuditLog:
        entry = AuditLog(**log_in.model_dump())
        db.add(entry)
        await db.commit()
        await db.refresh(entry)
        return entry

    @staticmethod
    async def get_audit_logs(db: AsyncSession, username: Optional[str] = None, limit: int = 100) -> List[AuditLogOut]:
        query = select(AuditLog)
        if username:
            query = query.where(AuditLog.username == username)
        result = await db.execute(query.order_by(AuditLog.timestamp.desc()).limit(limit))
        return [AuditLogOut.model_validate(e) for e in result.scalars().all()]
