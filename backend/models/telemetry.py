from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime
from datetime import datetime
from backend.models.base import BaseModel

class InterfaceMetricHistory(BaseModel):
    __tablename__ = "interface_metric_histories"

    interface_id = Column(Integer, ForeignKey("device_interfaces.id", ondelete="CASCADE"), nullable=False, index=True)
    inbound_bps = Column(Float, default=0.0)
    outbound_bps = Column(Float, default=0.0)
    utilization_pct = Column(Float, default=0.0)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

class SlaProbeHistory(BaseModel):
    __tablename__ = "sla_probe_histories"

    target_name = Column(String(100), nullable=False)
    ip_address = Column(String(45), nullable=False, index=True)
    rtt_ms = Column(Float, default=0.0)
    jitter_ms = Column(Float, default=0.0)
    packet_loss_pct = Column(Float, default=0.0)
    is_up = Column(Integer, default=1)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
