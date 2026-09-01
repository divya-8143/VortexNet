from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List

class InterfaceMetricOut(BaseModel):
    id: int
    interface_id: int
    inbound_bps: float
    outbound_bps: float
    utilization_pct: float
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)

class SlaProbeOut(BaseModel):
    id: int
    target_name: str
    ip_address: str
    rtt_ms: float
    jitter_ms: float
    packet_loss_pct: float
    is_up: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)

class BandwidthSummary(BaseModel):
    total_inbound_gbps: float
    total_outbound_gbps: float
    avg_utilization_pct: float
    top_utilized_interface: str
