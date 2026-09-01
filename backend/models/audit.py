import enum
from sqlalchemy import Column, String, Enum, Integer, DateTime, Text
from datetime import datetime
from backend.models.base import BaseModel

class ActionType(str, enum.Enum):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    EXECUTE = "EXECUTE"
    LOGIN = "LOGIN"
    CONFIG_BACKUP = "CONFIG_BACKUP"

class AuditLog(BaseModel):
    __tablename__ = "audit_logs"

    username = Column(String(50), nullable=False, index=True)
    action_type = Column(Enum(ActionType), nullable=False)
    module_name = Column(String(50), nullable=False, index=True)
    details = Column(Text, nullable=False)
    client_ip = Column(String(45), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

    def __repr__(self):
        return f"<AuditLog User={self.username} Action={self.action_type} Module={self.module_name}>"
