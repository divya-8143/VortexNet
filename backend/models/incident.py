import enum
from sqlalchemy import Column, String, Enum, Integer, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.models.base import BaseModel
from backend.models.alert import AlertSeverity

class IncidentStatus(str, enum.Enum):
    TRIGGERED = "TRIGGERED"
    ACKNOWLEDGED = "ACKNOWLEDGED"
    IN_PROGRESS = "IN_PROGRESS"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"

class Incident(BaseModel):
    __tablename__ = "incidents"

    title = Column(String(150), nullable=False)
    device_id = Column(Integer, ForeignKey("network_devices.id", ondelete="CASCADE"), nullable=False, index=True)
    severity = Column(Enum(AlertSeverity), default=AlertSeverity.WARNING, nullable=False)
    status = Column(Enum(IncidentStatus), default=IncidentStatus.TRIGGERED, nullable=False, index=True)
    description = Column(Text, nullable=False)
    assigned_to = Column(String(100), nullable=True, default="NOC Duty Engineer")
    triggered_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    acknowledged_at = Column(DateTime, nullable=True)
    resolved_at = Column(DateTime, nullable=True)
    resolution_notes = Column(Text, nullable=True)

    device = relationship("NetworkDevice", back_populates="incidents")

    def __repr__(self):
        return f"<Incident #{self.id} Title={self.title} Status={self.status} Severity={self.severity}>"
