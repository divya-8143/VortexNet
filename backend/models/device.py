import enum
from sqlalchemy import Column, String, Enum, Integer, Float, Boolean, Text
from sqlalchemy.orm import relationship
from backend.models.base import BaseModel

class DeviceType(str, enum.Enum):
    ROUTER = "ROUTER"
    SWITCH = "SWITCH"
    FIREWALL = "FIREWALL"
    ACCESS_POINT = "ACCESS_POINT"
    SERVER = "SERVER"
    LOAD_BALANCER = "LOAD_BALANCER"

class DeviceStatus(str, enum.Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"
    MAINTENANCE = "MAINTENANCE"

class VendorType(str, enum.Enum):
    CISCO = "CISCO"
    JUNIPER = "JUNIPER"
    ARISTA = "ARISTA"
    PALO_ALTO = "PALO_ALTO"
    FORTINET = "FORTINET"
    ARUBA = "ARUBA"
    LINUX = "LINUX"

class NetworkDevice(BaseModel):
    __tablename__ = "network_devices"

    hostname = Column(String(100), unique=True, index=True, nullable=False)
    management_ip = Column(String(45), unique=True, index=True, nullable=False)
    mac_address = Column(String(17), unique=True, nullable=False)
    device_type = Column(Enum(DeviceType), nullable=False, default=DeviceType.ROUTER)
    vendor = Column(Enum(VendorType), nullable=False, default=VendorType.CISCO)
    model = Column(String(100), nullable=False)
    firmware_version = Column(String(50), nullable=False)
    serial_number = Column(String(100), unique=True, nullable=False)
    location = Column(String(100), nullable=False, default="Data Center Alpha - Rack A1")
    status = Column(Enum(DeviceStatus), nullable=False, default=DeviceStatus.ONLINE)
    
    # Live telemetry state
    cpu_usage_pct = Column(Float, default=15.0)
    ram_usage_pct = Column(Float, default=32.0)
    temperature_celsius = Column(Float, default=38.5)
    uptime_seconds = Column(Integer, default=864000)
    
    # SNMP & Auth settings
    snmp_community = Column(String(50), default="public")
    snmp_version = Column(String(10), default="v2c")
    notes = Column(Text, nullable=True)

    interfaces = relationship("DeviceInterface", back_populates="device", cascade="all, delete-orphan")
    syslogs = relationship("SyslogEntry", back_populates="device", cascade="all, delete-orphan")
    incidents = relationship("Incident", back_populates="device", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<NetworkDevice hostname={self.hostname} ip={self.management_ip} status={self.status}>"
