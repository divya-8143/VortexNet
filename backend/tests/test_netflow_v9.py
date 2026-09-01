import pytest
from backend.simulation.netflow_simulator import NetFlowSimulator

def test_netflow_v9_exporter():
    batch = NetFlowSimulator.generate_flow_batch(count=5)
    assert len(batch) == 5
    for flow in batch:
        assert "application" in flow
        assert "protocol" in flow
