from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.route import RoutingTableEntry, ArpEntry
from backend.schemas.route import RouteCreate, ArpCreate

class RoutingService:
    @staticmethod
    async def get_device_routes(db: AsyncSession, device_id: int) -> List[RoutingTableEntry]:
        result = await db.execute(select(RoutingTableEntry).where(RoutingTableEntry.device_id == device_id).order_by(RoutingTableEntry.destination_cidr.asc()))
        return list(result.scalars().all())

    @staticmethod
    async def add_route(db: AsyncSession, route_in: RouteCreate) -> RoutingTableEntry:
        route = RoutingTableEntry(**route_in.model_dump())
        db.add(route)
        await db.commit()
        await db.refresh(route)
        return route

    @staticmethod
    async def get_device_arp_table(db: AsyncSession, device_id: int) -> List[ArpEntry]:
        result = await db.execute(select(ArpEntry).where(ArpEntry.device_id == device_id).order_by(ArpEntry.ip_address.asc()))
        return list(result.scalars().all())

    @staticmethod
    async def add_arp_entry(db: AsyncSession, arp_in: ArpCreate) -> ArpEntry:
        arp = ArpEntry(**arp_in.model_dump())
        db.add(arp)
        await db.commit()
        await db.refresh(arp)
        return arp
