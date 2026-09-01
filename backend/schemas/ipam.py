from pydantic import BaseModel, ConfigDict
from typing import Optional
from backend.models.ipam import IPStatus, SubnetCategory

class SubnetBase(BaseModel):
    cidr: str
    name: str
    vlan_id: Optional[int] = None
    category: SubnetCategory = SubnetCategory.MANAGEMENT
    gateway_ip: Optional[str] = None
    description: Optional[str] = None

class SubnetCreate(SubnetBase):
    pass

class SubnetOut(SubnetBase):
    id: int
    total_ips: int
    used_ips: int
    utilization_pct: float

    model_config = ConfigDict(from_attributes=True)

class IPAddressBase(BaseModel):
    ip_address: str
    mac_address: Optional[str] = None
    hostname: Optional[str] = None
    status: IPStatus = IPStatus.AVAILABLE
    dns_ptr_record: Optional[str] = None
    assigned_to: Optional[str] = None
    is_static: bool = True

class IPAddressCreate(IPAddressBase):
    subnet_id: int

class IPAddressUpdate(BaseModel):
    mac_address: Optional[str] = None
    hostname: Optional[str] = None
    status: Optional[IPStatus] = None
    dns_ptr_record: Optional[str] = None
    assigned_to: Optional[str] = None
    is_static: Optional[bool] = None

class IPAddressOut(IPAddressBase):
    id: int
    subnet_id: int

    model_config = ConfigDict(from_attributes=True)
