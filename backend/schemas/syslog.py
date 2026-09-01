from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from backend.models.syslog import SyslogSeverity, SyslogFacility

class SyslogCreate(BaseModel):
    device_id: int
    hostname: str
    facility: SyslogFacility = SyslogFacility.LOCAL0
    severity: SyslogSeverity = SyslogSeverity.INFO
    message: str

class SyslogOut(SyslogCreate):
    id: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)
