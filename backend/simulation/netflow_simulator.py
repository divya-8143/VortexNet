import random
from typing import List, Dict, Any

class NetFlowSimulator:
    """
    Generates synthetic NetFlow v9 / IPFIX flow records for Network Traffic Analytics
    """
    
    COMMON_PROTOCOLS = [
        {"name": "HTTPS", "port": 443, "proto": "TCP"},
        {"name": "HTTP", "port": 80, "proto": "TCP"},
        {"name": "SSH", "port": 22, "proto": "TCP"},
        {"name": "DNS", "port": 53, "proto": "UDP"},
        {"name": "BGP", "port": 179, "proto": "TCP"},
        {"name": "SNMP", "port": 161, "proto": "UDP"},
        {"name": "NTP", "port": 123, "proto": "UDP"},
        {"name": "IPsec", "port": 500, "proto": "UDP"}
    ]

    TOP_TALKER_IPS = [
        "10.0.1.15", "10.0.1.45", "10.0.2.108", "10.0.3.22",
        "172.16.10.5", "172.16.10.99", "192.168.1.50", "192.168.1.100"
    ]

    @staticmethod
    def generate_flow_batch(count: int = 20) -> List[Dict[str, Any]]:
        flows = []
        for _ in range(count):
            proto_info = random.choice(NetFlowSimulator.COMMON_PROTOCOLS)
            src_ip = random.choice(NetFlowSimulator.TOP_TALKER_IPS)
            dst_ip = f"198.51.100.{random.randint(1, 254)}"
            bytes_transferred = random.randint(1024, 15000000)
            packets_count = random.randint(10, 12000)

            flows.append({
                "src_ip": src_ip,
                "dst_ip": dst_ip,
                "src_port": random.randint(1024, 65535),
                "dst_port": proto_info["port"],
                "protocol": proto_info["proto"],
                "application": proto_info["name"],
                "bytes": bytes_transferred,
                "packets": packets_count,
                "duration_ms": random.randint(100, 5000)
            })
        return flows
