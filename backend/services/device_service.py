from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from fastapi import HTTPException, status
from backend.models.device import NetworkDevice, DeviceStatus
from backend.schemas.device import DeviceCreate, DeviceUpdate, DeviceSummary

class DeviceService:
    @staticmethod
    async def get_all_devices(db: AsyncSession, device_type: Optional[str] = None, status_filter: Optional[str] = None) -> List[NetworkDevice]:
        query = select(NetworkDevice)
        if device_type:
            query = query.where(NetworkDevice.device_type == device_type)
        if status_filter:
            query = query.where(NetworkDevice.status == status_filter)
        result = await db.execute(query.order_by(NetworkDevice.hostname.asc()))
        return list(result.scalars().all())

    @staticmethod
    async def get_device_by_id(db: AsyncSession, device_id: int) -> Optional[NetworkDevice]:
        result = await db.execute(select(NetworkDevice).where(NetworkDevice.id == device_id))
        return result.scalars().first()

    @staticmethod
    async def get_device_by_hostname(db: AsyncSession, hostname: str) -> Optional[NetworkDevice]:
        result = await db.execute(select(NetworkDevice).where(NetworkDevice.hostname == hostname))
        return result.scalars().first()

    @staticmethod
    async def create_device(db: AsyncSession, device_in: DeviceCreate) -> NetworkDevice:
        existing_host = await DeviceService.get_device_by_hostname(db, device_in.hostname)
        if existing_host:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Device hostname '{device_in.hostname}' already exists.")

        device = NetworkDevice(**device_in.model_dump())
        db.add(device)
        await db.commit()
        await db.refresh(device)
        return device

    @staticmethod
    async def update_device(db: AsyncSession, device_id: int, device_in: DeviceUpdate) -> NetworkDevice:
        device = await DeviceService.get_device_by_id(db, device_id)
        if not device:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Device {device_id} not found.")

        update_data = device_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(device, field, value)

        await db.commit()
        await db.refresh(device)
        return device

    @staticmethod
    async def delete_device(db: AsyncSession, device_id: int) -> bool:
        device = await DeviceService.get_device_by_id(db, device_id)
        if not device:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Device {device_id} not found.")
        await db.delete(device)
        await db.commit()
        return True

    @staticmethod
    async def get_device_summary(db: AsyncSession) -> DeviceSummary:
        devices = await DeviceService.get_all_devices(db)
        total = len(devices)
        if total == 0:
            return DeviceSummary(
                total_devices=0, online_count=0, offline_count=0, warning_count=0, critical_count=0, avg_cpu_pct=0.0, avg_ram_pct=0.0
            )

        online = sum(1 for d in devices if d.status == DeviceStatus.ONLINE)
        offline = sum(1 for d in devices if d.status == DeviceStatus.OFFLINE)
        warning = sum(1 for d in devices if d.status == DeviceStatus.WARNING)
        critical = sum(1 for d in devices if d.status == DeviceStatus.CRITICAL)
        
        avg_cpu = sum(d.cpu_usage_pct for d in devices) / total
        avg_ram = sum(d.ram_usage_pct for d in devices) / total

        return DeviceSummary(
            total_devices=total,
            online_count=online,
            offline_count=offline,
            warning_count=warning,
            critical_count=critical,
            avg_cpu_pct=round(avg_cpu, 2),
            avg_ram_pct=round(avg_ram, 2)
        )
