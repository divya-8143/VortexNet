import enum
from sqlalchemy import Column, String, Enum, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.models.base import BaseModel

class SyslogSeverity(str, enum.Enum):
    EMERGENCY = "EMERGENCY"
    ALERT = "ALERT"
    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    NOTICE = "NOTICE"
    INFO = "INFO"
    DEBUG = "DEBUG"

class SyslogFacility(str, enum.Enum):
    KERNEL = "KERNEL"
    USER = "USER"
    MAIL = "MAIL"
    DAEMON = "DAEMON"
    AUTH = "AUTH"
    SYSLOG = "SYSLOG"
    LOCAL0 = "LOCAL0"
    LOCAL1 = "LOCAL1"
    LOCAL2 = "LOCAL2"
    LOCAL3 = "LOCAL3"
    LOCAL4 = "LOCAL4"
    LOCAL5 = "LOCAL5"
    LOCAL6 = "LOCAL6"
    LOCAL7 = "LOCAL7"

class SyslogEntry(BaseModel):
    __tablename__ = "syslog_entries"

    device_id = Column(Integer, ForeignKey("network_devices.id", ondelete="CASCADE"), nullable=False, index=True)
    hostname = Column(String(100), nullable=False, index=True)
    facility = Column(Enum(SyslogFacility), default=SyslogFacility.LOCAL0, nullable=False)
    severity = Column(Enum(SyslogSeverity), default=SyslogSeverity.INFO, nullable=False, index=True)
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

    device = relationship("NetworkDevice", back_populates="syslogs")

    def __repr__(self):
        return f"<SyslogEntry [{self.severity}] {self.hostname}: {self.message[:40]}>"
