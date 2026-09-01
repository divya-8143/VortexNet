from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from backend.models.interface import DeviceInterface
from backend.models.vlan import VlanConfig
from backend.schemas.interface import InterfaceCreate, InterfaceUpdate
from backend.schemas.vlan import VlanCreate

class InterfaceService:
    @staticmethod
    async def get_device_interfaces(db: AsyncSession, device_id: int) -> List[DeviceInterface]:
        result = await db.execute(select(DeviceInterface).where(DeviceInterface.device_id == device_id).order_by(DeviceInterface.name.asc()))
        return list(result.scalars().all())

    @staticmethod
    async def get_interface_by_id(db: AsyncSession, interface_id: int) -> Optional[DeviceInterface]:
        result = await db.execute(select(DeviceInterface).where(DeviceInterface.id == interface_id))
        return result.scalars().first()

    @staticmethod
    async def create_interface(db: AsyncSession, interface_in: InterfaceCreate) -> DeviceInterface:
        interface = DeviceInterface(**interface_in.model_dump())
        db.add(interface)
        await db.commit()
        await db.refresh(interface)
        return interface

    @staticmethod
    async def update_interface(db: AsyncSession, interface_id: int, interface_in: InterfaceUpdate) -> DeviceInterface:
        interface = await InterfaceService.get_interface_by_id(db, interface_id)
        if not interface:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Interface {interface_id} not found.")

        update_data = interface_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(interface, field, value)

        await db.commit()
        await db.refresh(interface)
        return interface

class VlanService:
    @staticmethod
    async def get_device_vlans(db: AsyncSession, device_id: int) -> List[VlanConfig]:
        result = await db.execute(select(VlanConfig).where(VlanConfig.device_id == device_id).order_by(VlanConfig.vlan_id.asc()))
        return list(result.scalars().all())

    @staticmethod
    async def create_vlan(db: AsyncSession, vlan_in: VlanCreate) -> VlanConfig:
        vlan = VlanConfig(**vlan_in.model_dump())
        db.add(vlan)
        await db.commit()
        await db.refresh(vlan)
        return vlan
