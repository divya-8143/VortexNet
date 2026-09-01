from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from backend.models.audit import ActionType

class AuditLogBase(BaseModel):
    username: str
    action_type: ActionType
    module_name: str
    details: str
    client_ip: Optional[str] = "127.0.0.1"

class AuditLogCreate(AuditLogBase):
    pass

class AuditLogOut(AuditLogBase):
    id: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)
