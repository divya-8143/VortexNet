import enum
from sqlalchemy import Column, String, Enum, Integer, BigInteger, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.models.base import BaseModel

class InterfaceStatus(str, enum.Enum):
    UP = "UP"
    DOWN = "DOWN"
    ADMIN_DOWN = "ADMIN_DOWN"
    TESTING = "TESTING"

class InterfaceType(str, enum.Enum):
    ETHERNET = "ETHERNET"
    GIGABIT_ETHERNET = "GIGABIT_ETHERNET"
    TEN_GIGABIT = "TEN_GIGABIT"
    FORTY_GIGABIT = "FORTY_GIGABIT"
    HUNDRED_GIGABIT = "HUNDRED_GIGABIT"
    LOOPBACK = "LOOPBACK"
    VLAN_SVI = "VLAN_SVI"
    SERIAL = "SERIAL"

class DeviceInterface(BaseModel):
    __tablename__ = "device_interfaces"

    device_id = Column(Integer, ForeignKey("network_devices.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(50), nullable=False)  # e.g., GigabitEthernet0/0/1, eth0
    interface_type = Column(Enum(InterfaceType), default=InterfaceType.GIGABIT_ETHERNET, nullable=False)
    status = Column(Enum(InterfaceStatus), default=InterfaceStatus.UP, nullable=False)
    mac_address = Column(String(17), nullable=True)
    ip_address = Column(String(45), nullable=True)
    subnet_mask = Column(String(45), nullable=True)
    speed_mbps = Column(Integer, default=1000)
    mtu = Column(Integer, default=1500)
    duplex = Column(String(20), default="Full")
    is_trunk = Column(Boolean, default=False)
    vlan_id = Column(Integer, nullable=True, default=1)
    
    # Telemetry Counters
    rx_bytes = Column(BigInteger, default=0)
    tx_bytes = Column(BigInteger, default=0)
    rx_packets = Column(BigInteger, default=0)
    tx_packets = Column(BigInteger, default=0)
    rx_errors = Column(Integer, default=0)
    tx_errors = Column(Integer, default=0)
    rx_discards = Column(Integer, default=0)
    tx_discards = Column(Integer, default=0)

    device = relationship("NetworkDevice", back_populates="interfaces")

    def __repr__(self):
        return f"<DeviceInterface {self.name} on Device#{self.device_id} Status={self.status}>"
