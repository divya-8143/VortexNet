import enum
from sqlalchemy import Column, String, Enum, Integer, Boolean, ForeignKey
from backend.models.base import BaseModel

class IPStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    RESERVED = "RESERVED"
    AVAILABLE = "AVAILABLE"
    DHCP_LEASE = "DHCP_LEASE"
    CONFLICT = "CONFLICT"

class SubnetCategory(str, enum.Enum):
    MANAGEMENT = "MANAGEMENT"
    DATA_CENTER = "DATA_CENTER"
    VOIP = "VOIP"
    USER_LAN = "USER_LAN"
    DMZ = "DMZ"
    POINT_TO_POINT = "POINT_TO_POINT"

class Subnet(BaseModel):
    __tablename__ = "ipam_subnets"

    cidr = Column(String(50), unique=True, index=True, nullable=False) # e.g. 10.0.1.0/24
    name = Column(String(100), nullable=False)
    vlan_id = Column(Integer, nullable=True)
    category = Column(Enum(SubnetCategory), default=SubnetCategory.MANAGEMENT, nullable=False)
    gateway_ip = Column(String(45), nullable=True)
    description = Column(String(255), nullable=True)
    total_ips = Column(Integer, default=254)
    used_ips = Column(Integer, default=0)

    def __repr__(self):
        return f"<Subnet {self.cidr} name={self.name} category={self.category}>"

class IPAddress(BaseModel):
    __tablename__ = "ipam_addresses"

    subnet_id = Column(Integer, ForeignKey("ipam_subnets.id", ondelete="CASCADE"), nullable=False, index=True)
    ip_address = Column(String(45), unique=True, index=True, nullable=False)
    mac_address = Column(String(17), nullable=True)
    hostname = Column(String(100), nullable=True)
    status = Column(Enum(IPStatus), default=IPStatus.AVAILABLE, nullable=False)
    dns_ptr_record = Column(String(150), nullable=True)
    assigned_to = Column(String(100), nullable=True)
    is_static = Column(Boolean, default=True)

    def __repr__(self):
        return f"<IPAddress {self.ip_address} status={self.status} host={self.hostname}>"
