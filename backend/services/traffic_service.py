from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func, desc
from backend.models.traffic import NetFlowRecord
from backend.schemas.traffic import TopTalkerItem, ProtocolDistributionItem, NetFlowRecordOut
from backend.simulation.netflow_simulator import NetFlowSimulator

class TrafficService:
    @staticmethod
    async def get_recent_flows(db: AsyncSession, limit: int = 50) -> List[NetFlowRecordOut]:
        result = await db.execute(
            select(NetFlowRecord)
            .order_by(NetFlowRecord.timestamp.desc())
            .limit(limit)
        )
        return [NetFlowRecordOut.model_validate(r) for r in result.scalars().all()]

    @staticmethod
    async def get_top_talkers(db: AsyncSession, limit: int = 5) -> List[TopTalkerItem]:
        # Aggregate top source IPs from NetFlow records
        result = await db.execute(
            select(
                NetFlowRecord.src_ip,
                func.sum(NetFlowRecord.bytes_transferred).label("total_bytes"),
                func.sum(NetFlowRecord.packets_count).label("total_packets")
            )
            .group_by(NetFlowRecord.src_ip)
            .order_by(desc("total_bytes"))
            .limit(limit)
        )
        rows = result.all()
        
        grand_total = sum(r.total_bytes for r in rows) if rows else 1
        items = []
        for r in rows:
            pct = round((r.total_bytes / max(grand_total, 1)) * 100.0, 1)
            items.append(TopTalkerItem(
                ip_address=r.src_ip,
                total_bytes=r.total_bytes or 0,
                total_packets=r.total_packets or 0,
                percentage=pct
            ))
        return items

    @staticmethod
    async def get_protocol_distribution(db: AsyncSession) -> List[ProtocolDistributionItem]:
        result = await db.execute(
            select(
                NetFlowRecord.application,
                func.sum(NetFlowRecord.bytes_transferred).label("total_bytes")
            )
            .group_by(NetFlowRecord.application)
            .order_by(desc("total_bytes"))
        )
        rows = result.all()
        grand_total = sum(r.total_bytes for r in rows) if rows else 1
        items = []
        for r in rows:
            pct = round((r.total_bytes / max(grand_total, 1)) * 100.0, 1)
            items.append(ProtocolDistributionItem(
                protocol_name=r.application,
                bytes_count=r.total_bytes or 0,
                percentage=pct
            ))
        return items
