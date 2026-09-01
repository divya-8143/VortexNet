import enum
from sqlalchemy import Column, String, Enum, Integer, ForeignKey
from backend.models.base import BaseModel

class RouteProtocol(str, enum.Enum):
    STATIC = "STATIC"
    CONNECTED = "CONNECTED"
    OSPF = "OSPF"
    BGP = "BGP"
    EIGRP = "EIGRP"
    RIP = "RIP"

class RoutingTableEntry(BaseModel):
    __tablename__ = "routing_table_entries"

    device_id = Column(Integer, ForeignKey("network_devices.id", ondelete="CASCADE"), nullable=False, index=True)
    destination_cidr = Column(String(50), nullable=False)
    next_hop = Column(String(45), nullable=True)
    out_interface = Column(String(50), nullable=False)
    protocol = Column(Enum(RouteProtocol), default=RouteProtocol.STATIC, nullable=False)
    metric = Column(Integer, default=1)
    admin_distance = Column(Integer, default=1)

    def __repr__(self):
        return f"<Route {self.destination_cidr} via {self.next_hop} [{self.protocol}]>"

class ArpEntry(BaseModel):
    __tablename__ = "arp_entries"

    device_id = Column(Integer, ForeignKey("network_devices.id", ondelete="CASCADE"), nullable=False, index=True)
    ip_address = Column(String(45), nullable=False)
    mac_address = Column(String(17), nullable=False)
    interface_name = Column(String(50), nullable=False)
    age_minutes = Column(Integer, default=0)

    def __repr__(self):
        return f"<ArpEntry {self.ip_address} -> {self.mac_address}>"
