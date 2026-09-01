from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime
from backend.models.device import DeviceType, DeviceStatus, VendorType

class DeviceBase(BaseModel):
    hostname: str
    management_ip: str
    mac_address: str
    device_type: DeviceType = DeviceType.ROUTER
    vendor: VendorType = VendorType.CISCO
    model: str
    firmware_version: str
    serial_number: str
    location: str = "Data Center Alpha - Rack A1"
    snmp_community: Optional[str] = "public"
    snmp_version: Optional[str] = "v2c"
    notes: Optional[str] = None

class DeviceCreate(DeviceBase):
    pass

class DeviceUpdate(BaseModel):
    hostname: Optional[str] = None
    management_ip: Optional[str] = None
    mac_address: Optional[str] = None
    device_type: Optional[DeviceType] = None
    vendor: Optional[VendorType] = None
    model: Optional[str] = None
    firmware_version: Optional[str] = None
    location: Optional[str] = None
    status: Optional[DeviceStatus] = None
    notes: Optional[str] = None

class DeviceHealthUpdate(BaseModel):
    cpu_usage_pct: float
    ram_usage_pct: float
    temperature_celsius: float
    uptime_seconds: int
    status: DeviceStatus

class DeviceOut(DeviceBase):
    id: int
    status: DeviceStatus
    cpu_usage_pct: float
    ram_usage_pct: float
    temperature_celsius: float
    uptime_seconds: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DeviceSummary(BaseModel):
    total_devices: int
    online_count: int
    offline_count: int
    warning_count: int
    critical_count: int
    avg_cpu_pct: float
    avg_ram_pct: float
