"""
VortexNet IANA Registered Ports & Network Protocol Definitions
Maps TCP/UDP port numbers to application protocol names and descriptions.
"""

IANA_PORT_MAP = {
    20: {"name": "FTP-Data", "proto": "TCP", "descr": "File Transfer Protocol (Data)"},
    21: {"name": "FTP-Control", "proto": "TCP", "descr": "File Transfer Protocol (Control)"},
    22: {"name": "SSH", "proto": "TCP", "descr": "Secure Shell Protocol"},
    23: {"name": "Telnet", "proto": "TCP", "descr": "Unencrypted Telnet Protocol"},
    25: {"name": "SMTP", "proto": "TCP", "descr": "Simple Mail Transfer Protocol"},
    53: {"name": "DNS", "proto": "UDP/TCP", "descr": "Domain Name System"},
    67: {"name": "DHCP-Server", "proto": "UDP", "descr": "Dynamic Host Configuration Protocol (Server)"},
    68: {"name": "DHCP-Client", "proto": "UDP", "descr": "Dynamic Host Configuration Protocol (Client)"},
    69: {"name": "TFTP", "proto": "UDP", "descr": "Trivial File Transfer Protocol"},
    80: {"name": "HTTP", "proto": "TCP", "descr": "Hypertext Transfer Protocol"},
    110: {"name": "POP3", "proto": "TCP", "descr": "Post Office Protocol v3"},
    123: {"name": "NTP", "proto": "UDP", "descr": "Network Time Protocol"},
    143: {"name": "IMAP", "proto": "TCP", "descr": "Internet Message Access Protocol"},
    161: {"name": "SNMP", "proto": "UDP", "descr": "Simple Network Management Protocol"},
    162: {"name": "SNMP-Trap", "proto": "UDP", "descr": "SNMP Trap Notifications"},
    179: {"name": "BGP", "proto": "TCP", "descr": "Border Gateway Protocol"},
    389: {"name": "LDAP", "proto": "TCP", "descr": "Lightweight Directory Access Protocol"},
    443: {"name": "HTTPS", "proto": "TCP", "descr": "HTTP Secure over TLS/SSL"},
    445: {"name": "SMB", "proto": "TCP", "descr": "Microsoft Server Message Block"},
    500: {"name": "IKE/IPsec", "proto": "UDP", "descr": "Internet Key Exchange for IPsec VPN"},
    514: {"name": "Syslog", "proto": "UDP", "descr": "Syslog Protocol Daemon"},
    636: {"name": "LDAPS", "proto": "TCP", "descr": "LDAP over SSL"},
    873: {"name": "Rsync", "proto": "TCP", "descr": "Rsync File Synchronization"},
    993: {"name": "IMAPS", "proto": "TCP", "descr": "IMAP over SSL"},
    995: {"name": "POP3S", "proto": "TCP", "descr": "POP3 over SSL"},
    1433: {"name": "MSSQL", "proto": "TCP", "descr": "Microsoft SQL Server"},
    1521: {"name": "Oracle", "proto": "TCP", "descr": "Oracle Database Listener"},
    2049: {"name": "NFS", "proto": "TCP/UDP", "descr": "Network File System"},
    3306: {"name": "MySQL", "proto": "TCP", "descr": "MySQL Database Server"},
    3389: {"name": "RDP", "proto": "TCP", "descr": "Remote Desktop Protocol"},
    5432: {"name": "PostgreSQL", "proto": "TCP", "descr": "PostgreSQL Relational Database"},
    5900: {"name": "VNC", "proto": "TCP", "descr": "Virtual Network Computing"},
    6379: {"name": "Redis", "proto": "TCP", "descr": "Redis In-Memory Key-Value Store"},
    8080: {"name": "HTTP-Proxy", "proto": "TCP", "descr": "HTTP Alternate / Web Proxy"},
    8443: {"name": "HTTPS-Alt", "proto": "TCP", "descr": "HTTPS Alternate Port"},
    9090: {"name": "Prometheus", "proto": "TCP", "descr": "Prometheus Monitoring Server"},
    9092: {"name": "Kafka", "proto": "TCP", "descr": "Apache Kafka Message Broker"},
    9200: {"name": "Elasticsearch", "proto": "TCP", "descr": "Elasticsearch REST Cluster Engine"}
}

def get_service_info(port: int) -> dict:
    return IANA_PORT_MAP.get(port, {"name": f"Custom-Port-{port}", "proto": "TCP/UDP", "descr": "Unassigned or Enterprise Custom Port"})
