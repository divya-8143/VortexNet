import pytest
from backend.simulation.mib_definitions import get_extended_mib_tree
from backend.simulation.cli_config_generator import CLIConfigGenerator
from backend.simulation.oui_database import lookup_mac_vendor
from backend.simulation.iana_services import get_service_info
from backend.simulation.syslog_catalog import get_catalog_entry

def test_extended_mib_tree_generation():
    mib_tree = get_extended_mib_tree()
    assert len(mib_tree) > 50
    assert "1.3.6.1.2.1.1.1.0" in mib_tree
    assert mib_tree["1.3.6.1.2.1.1.1.0"]["name"] == "sysDescr"

def test_cli_config_generator_cisco_and_juniper():
    cisco_conf = CLIConfigGenerator.generate_cisco_ios(
        hostname="core-test-01",
        mgmt_ip="10.0.0.1",
        interfaces=[{"name": "GigabitEthernet0/0/1", "ip_address": "10.0.0.1"}]
    )
    assert "hostname core-test-01" in cisco_conf
    assert "router ospf 1" in cisco_conf
    assert "snmp-server community public RO" in cisco_conf

    juniper_conf = CLIConfigGenerator.generate_juniper_junos("juniper-test-01", "10.0.0.2")
    assert "host-name juniper-test-01;" in juniper_conf
    assert "protocols {" in juniper_conf

def test_mac_oui_vendor_lookup():
    vendor1 = lookup_mac_vendor("00:00:0C:11:22:33")
    assert "Cisco" in vendor1

    vendor2 = lookup_mac_vendor("00:05:85:AA:BB:CC")
    assert "Juniper" in vendor2

    vendor_unknown = lookup_mac_vendor("FF:FF:FF:00:00:00")
    assert vendor_unknown == "Generic IEEE Device"

def test_iana_port_lookup():
    info_ssh = get_service_info(22)
    assert info_ssh["name"] == "SSH"

    info_bgp = get_service_info(179)
    assert info_bgp["name"] == "BGP"

    info_custom = get_service_info(45678)
    assert "Custom-Port" in info_custom["name"]

def test_syslog_catalog_lookup():
    cat = get_catalog_entry("LINK-3-UPDOWN")
    assert cat["facility"] == "LOCAL1"
    assert cat["severity"] == "WARNING"
