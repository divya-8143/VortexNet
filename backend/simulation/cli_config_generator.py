"""
VortexNet Cisco IOS/NX-OS, Juniper JunOS, Arista EOS & Palo Alto PAN-OS Synthetic CLI Generator
Generates full multi-vendor device configurations for audit, backup, and restore simulations.
"""

class CLIConfigGenerator:
    @staticmethod
    def generate_cisco_ios(hostname: str, mgmt_ip: str, interfaces: list) -> str:
        lines = [
            f"! Command: show running-config",
            f"! Building configuration...",
            f"version 17.3",
            f"service timestamps debug datetime msec",
            f"service timestamps log datetime msec",
            f"service password-encryption",
            f"!",
            f"hostname {hostname}",
            f"!",
            f"boot-start-marker",
            f"boot-end-marker",
            f"!",
            f"vrf definition MGMT",
            f" address-family ipv4",
            f" exit-address-family",
            f"!",
            f"username admin privilege 15 secret 9 $9$vortexnet_encrypted_hash",
            f"!",
            f"ip domain name vortexnet.local",
            f"ip name-server 10.0.0.1",
            f"ip cef",
            f"no ip domain lookup",
            f"!"
        ]
        
        for iface in interfaces:
            lines.append(f"interface {iface.get('name', 'GigabitEthernet0/0')}")
            lines.append(f" description Configured by VortexNet Platform")
            if iface.get('ip_address'):
                lines.append(f" ip address {iface.get('ip_address')} 255.255.255.0")
            else:
                lines.append(f" no ip address")
            lines.append(f" duplex full")
            lines.append(f" speed 1000")
            lines.append(f" no shutdown")
            lines.append(f"!")

        lines.extend([
            f"router ospf 1",
            f" router-id {mgmt_ip}",
            f" network 10.0.0.0 0.255.255.255 area 0",
            f"!",
            f"router bgp 65001",
            f" bgp router-id {mgmt_ip}",
            f" bgp log-neighbor-changes",
            f" neighbor 10.0.0.2 remote-as 65002",
            f"!",
            f"snmp-server community public RO",
            f"snmp-server location Data Center Alpha - Rack A1",
            f"snmp-server contact netops@vortexnet.local",
            f"snmp-server enable traps snmp authentication linkup linkdown coldstart warmstart",
            f"!",
            f"line con 0",
            f" logging synchronous",
            f" stopbits 1",
            f"line vty 0 4",
            f" exec-timeout 15 0",
            f" login local",
            f" transport input ssh",
            f"!",
            f"end"
        ])
        return "\n".join(lines)

    @staticmethod
    def generate_juniper_junos(hostname: str, mgmt_ip: str) -> str:
        lines = [
            f"## JunOS 21.4R1 Software Release",
            f"system {{",
            f"    host-name {hostname};",
            f"    domain-name vortexnet.local;",
            f"    time-zone UTC;",
            f"    authentication-order [ password ];",
            f"    root-authentication {{",
            f"        encrypted-password \"$6$vortexnet$hash\";",
            f"    }}",
            f"    services {{",
            f"        ssh {{",
            f"            protocol-version v2;",
            f"        }}",
            f"        netconf {{",
            f"            ssh;",
            f"        }}",
            f"    }}",
            f"}}",
            f"interfaces {{",
            f"    ge-0/0/0 {{",
            f"        unit 0 {{",
            f"            family inet {{",
            f"                address {mgmt_ip}/24;",
            f"            }}",
            f"        }}",
            f"    }}",
            f"}}",
            f"protocols {{",
            f"    bgp {{",
            f"        group IBGP-PEERS {{",
            f"            type internal;",
            f"            local-as 65001;",
            f"            neighbor 10.0.0.2;",
            f"        }}",
            f"    }}",
            f"    ospf {{",
            f"        area 0.0.0.0 {{",
            f"            interface ge-0/0/0.0;",
            f"        }}",
            f"    }}",
            f"}}"
        ]
        return "\n".join(lines)
