import pytest
from backend.services.alert_service import AlertService
from backend.services.incident_service import IncidentService
from backend.schemas.alert import AlertRuleCreate
from backend.schemas.incident import IncidentCreate, IncidentUpdate
from backend.models.alert import MetricType, AlertSeverity
from backend.models.incident import IncidentStatus

@pytest.mark.asyncio
async def test_alert_rule_creation(async_db):
    rule_in = AlertRuleCreate(
        rule_name="Critical Memory Alert (>95%)",
        metric_type=MetricType.RAM_USAGE,
        threshold_value=95.0,
        severity=AlertSeverity.CRITICAL,
        description="Fires when RAM is nearly depleted"
    )
    rule = await AlertService.create_rule(async_db, rule_in)
    assert rule.id is not None
    assert rule.metric_type == MetricType.RAM_USAGE

@pytest.mark.asyncio
async def test_incident_lifecycle_workflow(async_db):
    inc_in = IncidentCreate(
        title="Interface Down Link Failure",
        device_id=1,
        severity=AlertSeverity.MAJOR,
        description="GigabitEthernet0/1 changed state to down"
    )
    inc = await IncidentService.create_incident(async_db, inc_in)
    assert inc.status == IncidentStatus.TRIGGERED

    # Acknowledge incident
    ack = await IncidentService.update_incident(async_db, inc.id, IncidentUpdate(status=IncidentStatus.ACKNOWLEDGED))
    assert ack.status == IncidentStatus.ACKNOWLEDGED
    assert ack.acknowledged_at is not None

    # Resolve incident
    res = await IncidentService.update_incident(async_db, inc.id, IncidentUpdate(status=IncidentStatus.RESOLVED, resolution_notes="Replaced faulty SFP module"))
    assert res.status == IncidentStatus.RESOLVED
    assert res.resolved_at is not None
    assert res.resolution_notes == "Replaced faulty SFP module"
