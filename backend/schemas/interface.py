from pydantic import BaseModel, ConfigDict
from typing import Optional
from backend.models.interface import InterfaceStatus, InterfaceType

class InterfaceBase(BaseModel):
    name: str
    interface_type: InterfaceType = InterfaceType.GIGABIT_ETHERNET
    status: InterfaceStatus = InterfaceStatus.UP
    mac_address: Optional[str] = None
    ip_address: Optional[str] = None
    subnet_mask: Optional[str] = None
    speed_mbps: int = 1000
    mtu: int = 1500
    duplex: str = "Full"
    is_trunk: bool = False
    vlan_id: Optional[int] = 1

class InterfaceCreate(InterfaceBase):
    device_id: int

class InterfaceUpdate(BaseModel):
    status: Optional[InterfaceStatus] = None
    ip_address: Optional[str] = None
    subnet_mask: Optional[str] = None
    speed_mbps: Optional[int] = None
    is_trunk: Optional[bool] = None
    vlan_id: Optional[int] = None

class InterfaceOut(InterfaceBase):
    id: int
    device_id: int
    rx_bytes: int
    tx_bytes: int
    rx_packets: int
    tx_packets: int
    rx_errors: int
    tx_errors: int

    model_config = ConfigDict(from_attributes=True)
