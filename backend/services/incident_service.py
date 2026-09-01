from datetime import datetime
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from backend.models.incident import Incident, IncidentStatus
from backend.schemas.incident import IncidentCreate, IncidentUpdate

class IncidentService:
    @staticmethod
    async def get_all_incidents(db: AsyncSession, status_filter: Optional[str] = None) -> List[Incident]:
        query = select(Incident)
        if status_filter:
            query = query.where(Incident.status == status_filter)
        result = await db.execute(query.order_by(Incident.triggered_at.desc()))
        return list(result.scalars().all())

    @staticmethod
    async def get_incident_by_id(db: AsyncSession, incident_id: int) -> Optional[Incident]:
        result = await db.execute(select(Incident).where(Incident.id == incident_id))
        return result.scalars().first()

    @staticmethod
    async def create_incident(db: AsyncSession, incident_in: IncidentCreate) -> Incident:
        incident = Incident(**incident_in.model_dump())
        db.add(incident)
        await db.commit()
        await db.refresh(incident)
        return incident

    @staticmethod
    async def update_incident(db: AsyncSession, incident_id: int, incident_in: IncidentUpdate) -> Incident:
        incident = await IncidentService.get_incident_by_id(db, incident_id)
        if not incident:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incident {incident_id} not found.")

        if incident_in.status == IncidentStatus.ACKNOWLEDGED and not incident.acknowledged_at:
            incident.acknowledged_at = datetime.utcnow()
        elif incident_in.status in [IncidentStatus.RESOLVED, IncidentStatus.CLOSED] and not incident.resolved_at:
            incident.resolved_at = datetime.utcnow()

        update_data = incident_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(incident, field, value)

        await db.commit()
        await db.refresh(incident)
        return incident
