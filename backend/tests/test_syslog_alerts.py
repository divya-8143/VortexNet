import pytest
from backend.simulation.syslog_catalog import get_catalog_entry

def test_syslog_pattern_match_trigger():
    entry = get_catalog_entry("SEC-4-LOGIN_FAILED")
    assert entry["facility"] == "AUTH"
    assert entry["severity"] == "CRITICAL"
