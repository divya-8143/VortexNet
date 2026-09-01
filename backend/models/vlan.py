from sqlalchemy import Column, String, Integer, ForeignKey
from backend.models.base import BaseModel

class VlanConfig(BaseModel):
    __tablename__ = "vlan_configs"

    vlan_id = Column(Integer, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    subnet_cidr = Column(String(50), nullable=True)
    device_id = Column(Integer, ForeignKey("network_devices.id", ondelete="CASCADE"), nullable=False, index=True)

    def __repr__(self):
        return f"<VlanConfig VLAN{self.vlan_id} name={self.name}>"
