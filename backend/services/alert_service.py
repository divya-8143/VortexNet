from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from backend.models.alert import AlertRule
from backend.schemas.alert import AlertRuleCreate

class AlertService:
    @staticmethod
    async def get_all_rules(db: AsyncSession) -> List[AlertRule]:
        result = await db.execute(select(AlertRule).order_by(AlertRule.id.asc()))
        return list(result.scalars().all())

    @staticmethod
    async def create_rule(db: AsyncSession, rule_in: AlertRuleCreate) -> AlertRule:
        rule = AlertRule(**rule_in.model_dump())
        db.add(rule)
        await db.commit()
        await db.refresh(rule)
        return rule
