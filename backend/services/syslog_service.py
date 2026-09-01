from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.syslog import SyslogEntry, SyslogSeverity
from backend.schemas.syslog import SyslogCreate, SyslogOut

class SyslogService:
    @staticmethod
    async def get_syslogs(
        db: AsyncSession,
        severity: Optional[str] = None,
        search_query: Optional[str] = None,
        limit: int = 100
    ) -> List[SyslogOut]:
        query = select(SyslogEntry)
        if severity:
            query = query.where(SyslogEntry.severity == severity)
        if search_query:
            query = query.where(SyslogEntry.message.ilike(f"%{search_query}%"))

        result = await db.execute(query.order_by(SyslogEntry.timestamp.desc()).limit(limit))
        entries = result.scalars().all()
        return [SyslogOut.model_validate(e) for e in entries]

    @staticmethod
    async def ingest_log(db: AsyncSession, log_in: SyslogCreate) -> SyslogEntry:
        entry = SyslogEntry(**log_in.model_dump())
        db.add(entry)
        await db.commit()
        await db.refresh(entry)
        return entry
