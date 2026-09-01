import pytest
from backend.services.syslog_service import SyslogService
from backend.schemas.syslog import SyslogCreate
from backend.models.syslog import SyslogSeverity, SyslogFacility

@pytest.mark.asyncio
async def test_syslog_ingestion_and_filtering(async_db):
    log_in = SyslogCreate(
        device_id=1,
        hostname="core-router-01",
        facility=SyslogFacility.LOCAL0,
        severity=SyslogSeverity.WARNING,
        message="%LINK-3-UPDOWN: Interface GigabitEthernet0/0/1 down"
    )
    entry = await SyslogService.ingest_log(async_db, log_in)
    assert entry.id is not None

    logs = await SyslogService.get_syslogs(async_db, severity="WARNING")
    assert len(logs) >= 1
    assert logs[0].hostname == "core-router-01"

@pytest.mark.asyncio
async def test_syslog_search_query(async_db):
    log_in = SyslogCreate(
        device_id=1,
        hostname="edge-firewall-01",
        facility=SyslogFacility.AUTH,
        severity=SyslogSeverity.CRITICAL,
        message="SEC-4-LOGIN_FAILED: Unauthorized SSH connection attempt"
    )
    await SyslogService.ingest_log(async_db, log_in)

    results = await SyslogService.get_syslogs(async_db, search_query="Unauthorized SSH")
    assert len(results) >= 1
    assert "Unauthorized SSH" in results[0].message
