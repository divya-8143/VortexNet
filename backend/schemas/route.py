from pydantic import BaseModel, ConfigDict
from typing import Optional
from backend.models.route import RouteProtocol

class RouteBase(BaseModel):
    destination_cidr: str
    next_hop: Optional[str] = None
    out_interface: str
    protocol: RouteProtocol = RouteProtocol.STATIC
    metric: int = 1
    admin_distance: int = 1

class RouteCreate(RouteBase):
    device_id: int

class RouteOut(RouteBase):
    id: int
    device_id: int

    model_config = ConfigDict(from_attributes=True)

class ArpBase(BaseModel):
    ip_address: str
    mac_address: str
    interface_name: str
    age_minutes: int = 0

class ArpCreate(ArpBase):
    device_id: int

class ArpOut(ArpBase):
    id: int
    device_id: int

    model_config = ConfigDict(from_attributes=True)
