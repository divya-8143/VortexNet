from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.topology import TopologyLink
from backend.models.device import NetworkDevice
from backend.schemas.topology import LinkCreate, TopologyGraphData, LinkOut
from backend.schemas.device import DeviceOut

class TopologyService:
    @staticmethod
    async def get_all_links(db: AsyncSession) -> List[TopologyLink]:
        result = await db.execute(select(TopologyLink).order_by(TopologyLink.id.asc()))
        return list(result.scalars().all())

    @staticmethod
    async def create_link(db: AsyncSession, link_in: LinkCreate) -> TopologyLink:
        link = TopologyLink(**link_in.model_dump())
        db.add(link)
        await db.commit()
        await db.refresh(link)
        return link

    @staticmethod
    async def get_topology_graph(db: AsyncSession) -> TopologyGraphData:
        dev_res = await db.execute(select(NetworkDevice).order_by(NetworkDevice.hostname.asc()))
        devices = [DeviceOut.model_validate(d) for d in dev_res.scalars().all()]

        link_res = await db.execute(select(TopologyLink))
        links = [LinkOut.model_validate(l) for l in link_res.scalars().all()]

        return TopologyGraphData(nodes=devices, edges=links)
