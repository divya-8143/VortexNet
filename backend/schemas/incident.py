from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from backend.models.alert import AlertSeverity
from backend.models.incident import IncidentStatus

class IncidentBase(BaseModel):
    title: str
    device_id: int
    severity: AlertSeverity = AlertSeverity.WARNING
    description: str
    assigned_to: Optional[str] = "NOC Duty Engineer"

class IncidentCreate(IncidentBase):
    pass

class IncidentUpdate(BaseModel):
    status: Optional[IncidentStatus] = None
    assigned_to: Optional[str] = None
    resolution_notes: Optional[str] = None

class IncidentOut(IncidentBase):
    id: int
    status: IncidentStatus
    triggered_at: datetime
    acknowledged_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None
    resolution_notes: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
