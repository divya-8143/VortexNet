import random
from typing import Dict, Any

class ICMPSimulator:
    """
    Simulates ICMP Ping Echo probes and HTTP SLA response time checks
    """
    
    @staticmethod
    def probe_device(ip_address: str, is_online: bool = True) -> Dict[str, Any]:
        if not is_online:
            return {
                "ip_address": ip_address,
                "reachable": False,
                "rtt_ms": 0.0,
                "jitter_ms": 0.0,
                "packet_loss_pct": 100.0,
                "status_code": "TIMEOUT"
            }

        # Simulate small normal variance vs occasional latency spike
        spike = random.random() < 0.05
        base_rtt = random.uniform(45.0, 180.0) if spike else random.uniform(1.2, 18.5)
        loss = random.choice([0.0, 0.0, 0.0, 0.0, 2.5]) if spike else 0.0

        return {
            "ip_address": ip_address,
            "reachable": True,
            "rtt_ms": round(base_rtt, 2),
            "jitter_ms": round(random.uniform(0.1, 3.5), 2),
            "packet_loss_pct": loss,
            "status_code": "200 OK"
        }
