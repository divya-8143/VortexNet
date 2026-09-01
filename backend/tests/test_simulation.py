from backend.simulation.snmp_simulator import SNMPSimulator
from backend.simulation.netflow_simulator import NetFlowSimulator
from backend.simulation.icmp_simulator import ICMPSimulator
from backend.simulation.syslog_simulator import SyslogSimulator

def test_snmp_telemetry_generator():
    data = SNMPSimulator.get_snmp_telemetry("core-router-01", "CISCO", 25.0, 40.0)
    assert data["hostname"] == "core-router-01"
    assert "cpu_usage_pct" in data
    assert "ram_usage_pct" in data
    assert "temperature_celsius" in data
    assert 2.0 <= data["cpu_usage_pct"] <= 99.0

def test_netflow_batch_generator():
    flows = NetFlowSimulator.generate_flow_batch(count=10)
    assert len(flows) == 10
    assert "src_ip" in flows[0]
    assert "dst_ip" in flows[0]
    assert flows[0]["bytes"] > 0

def test_icmp_probe_simulator():
    probe_online = ICMPSimulator.probe_device("10.0.0.1", is_online=True)
    assert probe_online["reachable"] is True
    assert probe_online["rtt_ms"] > 0

    probe_offline = ICMPSimulator.probe_device("10.0.0.99", is_online=False)
    assert probe_offline["reachable"] is False
    assert probe_offline["packet_loss_pct"] == 100.0

def test_syslog_simulator():
    log = SyslogSimulator.generate_syslog(1, "dist-switch-01", "10.0.0.11")
    assert log["device_id"] == 1
    assert log["hostname"] == "dist-switch-01"
    assert "message" in log
