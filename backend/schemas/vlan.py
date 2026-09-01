from pydantic import BaseModel, ConfigDict
from typing import Optional

class VlanBase(BaseModel):
    vlan_id: int
    name: str
    description: Optional[str] = None
    subnet_cidr: Optional[str] = None

class VlanCreate(VlanBase):
    device_id: int

class VlanOut(VlanBase):
    id: int
    device_id: int

    model_config = ConfigDict(from_attributes=True)
