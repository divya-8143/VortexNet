import random
from typing import Dict, Any

class SNMPSimulator:
    """
    Simulates SNMP v2c/v3 MIB-II (RFC 1213) and HOST-RESOURCES-MIB data queries
    """
    
    MIB_OIDS = {
        "sysDescr": "1.3.6.1.2.1.1.1.0",
        "sysObjectID": "1.3.6.1.2.1.1.2.0",
        "sysUpTime": "1.3.6.1.2.1.1.3.0",
        "ifNumber": "1.3.6.1.2.1.2.1.0",
        "hrProcessorLoad": "1.3.6.1.2.1.25.3.3.1.2",
        "hrStorageUsed": "1.3.6.1.2.1.25.2.3.1.6"
    }

    @staticmethod
    def get_snmp_telemetry(hostname: str, vendor: str, current_cpu: float, current_ram: float) -> Dict[str, Any]:
        # Generate realistic random drift for telemetry metrics
        cpu_drift = random.uniform(-3.5, 3.5)
        ram_drift = random.uniform(-1.2, 1.2)
        temp_drift = random.uniform(-0.5, 0.5)

        new_cpu = max(2.0, min(99.0, current_cpu + cpu_drift))
        new_ram = max(10.0, min(98.0, current_ram + ram_drift))
        
        return {
            "hostname": hostname,
            "vendor": vendor,
            "snmp_status": "SUCCESS",
            "cpu_usage_pct": round(new_cpu, 2),
            "ram_usage_pct": round(new_ram, 2),
            "temperature_celsius": round(35.0 + (new_cpu * 0.35) + temp_drift, 1),
            "sys_uptime_ticks": random.randint(100000, 9000000),
            "oids_polled": len(SNMPSimulator.MIB_OIDS)
        }
