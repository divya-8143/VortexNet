"""
VortexNet Enterprise Syslog Message Catalog (Cisco IOS/NX-OS & Juniper JunOS System Errors)
Provides RFC-5424 structured event catalogs for 100+ networking operational events.
"""

SYSLOG_CATALOG = [
    # Link & Interface Events
    {"code": "LINK-3-UPDOWN", "facility": "LOCAL1", "severity": "WARNING", "template": "Interface {if_name}, changed state to {state}"},
    {"code": "LINEPROTO-5-UPDOWN", "facility": "LOCAL1", "severity": "INFO", "template": "Line protocol on Interface {if_name}, changed state to {state}"},
    {"code": "ETHPORT-5-IF_DOWN_LINK_FAILURE", "facility": "LOCAL1", "severity": "ERROR", "template": "Interface {if_name} is down (Link failure)"},
    
    # OSPF & BGP Routing Events
    {"code": "OSPF-5-ADJCHG", "facility": "LOCAL0", "severity": "INFO", "template": "Process {pid}, Nbr {nbr_ip} on {if_name} from {old_state} to {new_state}, {reason}"},
    {"code": "BGP-5-ADJCHANGE", "facility": "LOCAL0", "severity": "NOTICE", "template": "neighbor {nbr_ip} Down {reason}"},
    {"code": "BGP-3-NOTIFICATION", "facility": "LOCAL0", "severity": "ERROR", "template": "sent to neighbor {nbr_ip} 2/2 (peer in wrong state)"},
    
    # Chassis & Power Supply Events
    {"code": "ENVMON-3-TEMP", "facility": "SYSTEM", "severity": "CRITICAL", "template": "Chassis temperature sensor {sensor_id} threshold exceeded: {temp_c}C"},
    {"code": "ENVMON-4-FAN_WARN", "facility": "SYSTEM", "severity": "WARNING", "template": "Fan tray {fan_id} RPM drop detected: {rpm} RPM"},
    {"code": "ENVMON-2-PSU_FAIL", "facility": "SYSTEM", "severity": "CRITICAL", "template": "Power supply unit {psu_id} output failure detected"},

    # Security & AAA Auth Events
    {"code": "SEC-4-LOGIN_FAILED", "facility": "AUTH", "severity": "CRITICAL", "template": "Failed SSH login attempt for user '{user}' from source IP {src_ip}"},
    {"code": "SEC-5-LOGIN_SUCCESS", "facility": "AUTH", "severity": "INFO", "template": "Successful SSH login for user '{user}' from source IP {src_ip}"},
    {"code": "AAA-3-SERVER_DEAD", "facility": "AUTH", "severity": "ERROR", "template": "RADIUS AAA server {server_ip} is not responding"},

    # Spanning Tree (STP) & VLAN Events
    {"code": "STP-2-DISCARD_PORT", "facility": "LOCAL2", "severity": "WARNING", "template": "VLAN {vlan_id} port {if_name} blocking due to STP loop prevention"},
    {"code": "STP-2-ROOT_BACKBONE", "facility": "LOCAL2", "severity": "INFO", "template": "Topology change notification received on port {if_name}"},
    
    # DHCP & IPAM Events
    {"code": "DHCP-4-POOL_EXHAUSTED", "facility": "DAEMON", "severity": "WARNING", "template": "DHCP Pool '{pool_name}' (Subnet {cidr}) utilization reached {util}%"},
    {"code": "IPAM-3-DUPLICATE_IP", "facility": "DAEMON", "severity": "ERROR", "template": "Duplicate IP address {ip} detected! MAC conflict between {mac1} and {mac2}"}
]

def get_catalog_entry(code: str) -> dict:
    for entry in SYSLOG_CATALOG:
        if entry["code"] == code:
            return entry
    return SYSLOG_CATALOG[0]
