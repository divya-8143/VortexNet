from pydantic import BaseModel, ConfigDict
from typing import Optional
from backend.models.alert import AlertSeverity, MetricType

class AlertRuleBase(BaseModel):
    rule_name: str
    metric_type: MetricType
    threshold_value: float
    severity: AlertSeverity = AlertSeverity.WARNING
    is_enabled: bool = True
    description: Optional[str] = None

class AlertRuleCreate(AlertRuleBase):
    pass

class AlertRuleOut(AlertRuleBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
