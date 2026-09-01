import random
from datetime import datetime, timedelta
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.telemetry import InterfaceMetricHistory, SlaProbeHistory
from backend.schemas.telemetry import InterfaceMetricOut, SlaProbeOut, BandwidthSummary

class TelemetryService:
    @staticmethod
    async def get_interface_metrics(db: AsyncSession, interface_id: int, limit: int = 30) -> List[InterfaceMetricOut]:
        result = await db.execute(
            select(InterfaceMetricHistory)
            .where(InterfaceMetricHistory.interface_id == interface_id)
            .order_by(InterfaceMetricHistory.timestamp.desc())
            .limit(limit)
        )
        items = list(result.scalars().all())
        items.reverse()
        return [InterfaceMetricOut.model_validate(i) for i in items]

    @staticmethod
    async def get_sla_probes(db: AsyncSession, limit: int = 50) -> List[SlaProbeOut]:
        result = await db.execute(
            select(SlaProbeHistory)
            .order_by(SlaProbeHistory.timestamp.desc())
            .limit(limit)
        )
        return [SlaProbeOut.model_validate(i) for i in result.scalars().all()]

    @staticmethod
    async def get_bandwidth_summary(db: AsyncSession) -> BandwidthSummary:
        # Generate synthetic real-time bandwidth metrics summary
        inbound = round(random.uniform(14.2, 38.6), 2)
        outbound = round(random.uniform(12.8, 31.4), 2)
        avg_util = round(random.uniform(22.5, 58.4), 1)
        
        return BandwidthSummary(
            total_inbound_gbps=inbound,
            total_outbound_gbps=outbound,
            avg_utilization_pct=avg_util,
            top_utilized_interface="Core-Router-01 (Gi0/0/1 - 10G Trunk)"
        )
