import enum
from sqlalchemy import Column, String, Enum, Integer, Float, ForeignKey
from backend.models.base import BaseModel

class LinkType(str, enum.Enum):
    TRUNK = "TRUNK"
    ACCESS = "ACCESS"
    WAN = "WAN"
    VPN = "VPN"
    CROSS_CONNECT = "CROSS_CONNECT"

class LinkStatus(str, enum.Enum):
    HEALTHY = "HEALTHY"
    DEGRADED = "DEGRADED"
    DOWN = "DOWN"

class TopologyLink(BaseModel):
    __tablename__ = "topology_links"

    source_device_id = Column(Integer, ForeignKey("network_devices.id", ondelete="CASCADE"), nullable=False, index=True)
    source_interface = Column(String(50), nullable=False)
    target_device_id = Column(Integer, ForeignKey("network_devices.id", ondelete="CASCADE"), nullable=False, index=True)
    target_interface = Column(String(50), nullable=False)
    link_type = Column(Enum(LinkType), default=LinkType.TRUNK, nullable=False)
    capacity_gbps = Column(Float, default=10.0)
    current_utilization_pct = Column(Float, default=25.0)
    status = Column(Enum(LinkStatus), default=LinkStatus.HEALTHY, nullable=False)
    latency_ms = Column(Float, default=1.2)

    def __repr__(self):
        return f"<TopologyLink Src={self.source_device_id}:{self.source_interface} -> Tgt={self.target_device_id}:{self.target_interface} [{self.status}]>"
