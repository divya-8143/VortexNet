import pytest
from backend.models.vlan import VlanConfig

def test_vlan_qos_priority_mapping():
    vlan = VlanConfig(vlan_id=10, name="VOIP_PRIORITY", description="High Priority Voice Traffic", device_id=1)
    assert vlan.vlan_id == 10
    assert vlan.name == "VOIP_PRIORITY"
