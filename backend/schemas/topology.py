from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from backend.models.topology import LinkType, LinkStatus
from backend.schemas.device import DeviceOut

class LinkBase(BaseModel):
    source_device_id: int
    source_interface: str
    target_device_id: int
    target_interface: str
    link_type: LinkType = LinkType.TRUNK
    capacity_gbps: float = 10.0
    current_utilization_pct: float = 25.0
    status: LinkStatus = LinkStatus.HEALTHY
    latency_ms: float = 1.2

class LinkCreate(LinkBase):
    pass

class LinkOut(LinkBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

class TopologyGraphData(BaseModel):
    nodes: List[DeviceOut]
    edges: List[LinkOut]
