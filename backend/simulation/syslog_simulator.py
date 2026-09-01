import random
from typing import Dict, Any

class SyslogSimulator:
    """
    Generates RFC 5424 formatted synthetic syslog messages for network event streams
    """

    LOG_TEMPLATES = [
        {"severity": "INFO", "facility": "LOCAL0", "msg": "%OSPF-5-ADJCHG: Process 1, Nbr {nbr_ip} on {if_name} from FULL to DOWN, Neighbor Down: Dead timer expired"},
        {"severity": "WARNING", "facility": "LOCAL1", "msg": "%LINK-3-UPDOWN: Interface {if_name}, changed state to down"},
        {"severity": "ERROR", "facility": "SYSTEM", "msg": "%SYS-2-BADSHARE: Bad share count for buffer pool on {hostname}"},
        {"severity": "CRITICAL", "facility": "AUTH", "msg": "SEC-4-LOGIN_FAILED: Failed SSH login attempt for user 'admin' from {src_ip}"},
        {"severity": "NOTICE", "facility": "LOCAL2", "msg": "%BGP-5-ADJCHANGE: neighbor {nbr_ip} Up"},
        {"severity": "INFO", "facility": "DAEMON", "msg": "DHCP-POOL-UTILIZATION: Subnet 10.0.1.0/24 capacity reached 78%"}
    ]

    @staticmethod
    def generate_syslog(device_id: int, hostname: str, mgmt_ip: str) -> Dict[str, Any]:
        template = random.choice(SyslogSimulator.LOG_TEMPLATES)
        if_names = ["GigabitEthernet0/1", "GigabitEthernet0/2", "TenGigabitEthernet1/0/1", "eth0"]
        nbr_ips = ["10.0.1.2", "10.0.2.1", "172.16.1.5", "192.168.10.1"]
        src_ips = ["198.51.100.45", "203.0.113.12", "10.0.99.5"]

        msg = template["msg"].format(
            if_name=random.choice(if_names),
            nbr_ip=random.choice(nbr_ips),
            src_ip=random.choice(src_ips),
            hostname=hostname
        )

        return {
            "device_id": device_id,
            "hostname": hostname,
            "facility": template["facility"],
            "severity": template["severity"],
            "message": msg
        }
