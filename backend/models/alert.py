import enum
from sqlalchemy import Column, String, Enum, Float, Boolean
from backend.models.base import BaseModel

class AlertSeverity(str, enum.Enum):
    CRITICAL = "CRITICAL"
    MAJOR = "MAJOR"
    MINOR = "MINOR"
    WARNING = "WARNING"
    INFO = "INFO"

class MetricType(str, enum.Enum):
    CPU_USAGE = "CPU_USAGE"
    RAM_USAGE = "RAM_USAGE"
    TEMPERATURE = "TEMPERATURE"
    BANDWIDTH_UTILIZATION = "BANDWIDTH_UTILIZATION"
    PACKET_LOSS = "PACKET_LOSS"
    INTERFACE_STATUS = "INTERFACE_STATUS"

class AlertRule(BaseModel):
    __tablename__ = "alert_rules"

    rule_name = Column(String(100), unique=True, index=True, nullable=False)
    metric_type = Column(Enum(MetricType), nullable=False)
    threshold_value = Column(Float, nullable=False)
    severity = Column(Enum(AlertSeverity), default=AlertSeverity.WARNING, nullable=False)
    is_enabled = Column(Boolean, default=True, nullable=False)
    description = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<AlertRule {self.rule_name} Metric={self.metric_type} Threshold={self.threshold_value}>"
