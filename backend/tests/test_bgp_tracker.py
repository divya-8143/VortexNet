import pytest
from backend.models.route import RoutingTableEntry, RouteProtocol

def test_bgp_route_entry_validation():
    route = RoutingTableEntry(
        device_id=1,
        destination_cidr="0.0.0.0/0",
        next_hop="198.51.100.1",
        out_interface="TenGigabitEthernet1/0/1",
        protocol=RouteProtocol.BGP,
        metric=20
    )
    assert route.protocol == RouteProtocol.BGP
    assert route.next_hop == "198.51.100.1"
