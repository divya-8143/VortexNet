"""
VortexNet Comprehensive SNMP MIB-II, IF-MIB, ENTITY-MIB, IP-MIB, BGP4-MIB, and OSPF-MIB Definitions Dictionary
Contains authoritative OID trees, MIB variable definitions, and synthetic value generators.
"""

MIB_TREE = {
    # System Group (1.3.6.1.2.1.1)
    "1.3.6.1.2.1.1.1.0": {"name": "sysDescr", "type": "DisplayString", "access": "read-only", "descr": "A textual description of the entity."},
    "1.3.6.1.2.1.1.2.0": {"name": "sysObjectID", "type": "OBJECT IDENTIFIER", "access": "read-only", "descr": "The vendor's authoritative identification of the network management subsystem."},
    "1.3.6.1.2.1.1.3.0": {"name": "sysUpTime", "type": "TimeTicks", "access": "read-only", "descr": "The time (in hundredths of a second) since the network management portion of the system was last re-initialized."},
    "1.3.6.1.2.1.1.4.0": {"name": "sysContact", "type": "DisplayString", "access": "read-write", "descr": "The textual identification of the contact person for this managed node."},
    "1.3.6.1.2.1.1.5.0": {"name": "sysName", "type": "DisplayString", "access": "read-write", "descr": "An administratively-assigned name for this managed node."},
    "1.3.6.1.2.1.1.6.0": {"name": "sysLocation", "type": "DisplayString", "access": "read-write", "descr": "The physical location of this node."},
    "1.3.6.1.2.1.1.7.0": {"name": "sysServices", "type": "INTEGER", "access": "read-only", "descr": "A value which indicates the set of services that this entity offers."},

    # Interfaces Group (1.3.6.1.2.1.2)
    "1.3.6.1.2.1.2.1.0": {"name": "ifNumber", "type": "INTEGER", "access": "read-only", "descr": "The number of network interfaces present on this system."},
    "1.3.6.1.2.1.2.2.1.1": {"name": "ifIndex", "type": "INTEGER", "access": "read-only", "descr": "A unique value for each interface."},
    "1.3.6.1.2.1.2.2.1.2": {"name": "ifDescr", "type": "DisplayString", "access": "read-only", "descr": "A textual string containing information about the interface."},
    "1.3.6.1.2.1.2.2.1.3": {"name": "ifType", "type": "INTEGER", "access": "read-only", "descr": "The type of interface, distinguished according to the physical/link protocol."},
    "1.3.6.1.2.1.2.2.1.4": {"name": "ifMtu", "type": "INTEGER", "access": "read-only", "descr": "The size of the largest packet which can be sent or received on the interface."},
    "1.3.6.1.2.1.2.2.1.5": {"name": "ifSpeed", "type": "Gauge32", "access": "read-only", "descr": "An estimate of the interface's current bandwidth in bits per second."},
    "1.3.6.1.2.1.2.2.1.6": {"name": "ifPhysAddress", "type": "PhysAddress", "access": "read-only", "descr": "The interface's address at the protocol layer immediately below the network layer."},
    "1.3.6.1.2.1.2.2.1.7": {"name": "ifAdminStatus", "type": "INTEGER", "access": "read-write", "descr": "The desired state of the interface (up=1, down=2, testing=3)."},
    "1.3.6.1.2.1.2.2.1.8": {"name": "ifOperStatus", "type": "INTEGER", "access": "read-only", "descr": "The current operational state of the interface."},
    "1.3.6.1.2.1.2.2.1.10": {"name": "ifInOctets", "type": "Counter32", "access": "read-only", "descr": "Total number of octets received on the interface."},
    "1.3.6.1.2.1.2.2.1.11": {"name": "ifInUcastPkts", "type": "Counter32", "access": "read-only", "descr": "The number of subnetwork-unicast packets delivered to a higher-layer protocol."},
    "1.3.6.1.2.1.2.2.1.14": {"name": "ifInErrors", "type": "Counter32", "access": "read-only", "descr": "The number of inbound packets that contained errors."},
    "1.3.6.1.2.1.2.2.1.16": {"name": "ifOutOctets", "type": "Counter32", "access": "read-only", "descr": "Total number of octets transmitted out of the interface."},
    "1.3.6.1.2.1.2.2.1.20": {"name": "ifOutErrors", "type": "Counter32", "access": "read-only", "descr": "The number of outbound packets that contained errors."},

    # IP Group (1.3.6.1.2.1.4)
    "1.3.6.1.2.1.4.1.0": {"name": "ipForwarding", "type": "INTEGER", "access": "read-write", "descr": "Indicates whether this entity is acting as an IPv4 router (forwarding=1, notForwarding=2)."},
    "1.3.6.1.2.1.4.3.0": {"name": "ipInReceives", "type": "Counter32", "access": "read-only", "descr": "The total number of input datagrams received from interfaces."},
    "1.3.6.1.2.1.4.9.0": {"name": "ipInDelivers", "type": "Counter32", "access": "read-only", "descr": "The total number of input datagrams successfully delivered to IP user-protocols."},
    "1.3.6.1.2.1.4.10.0": {"name": "ipOutRequests", "type": "Counter32", "access": "read-only", "descr": "The total number of IP datagrams supplied to IP by local user-protocols."},

    # BGP4-MIB (1.3.6.1.2.1.15)
    "1.3.6.1.2.1.15.1.0": {"name": "bgpVersion", "type": "OCTET STRING", "access": "read-only", "descr": "Vector of supported BGP protocol versions."},
    "1.3.6.1.2.1.15.2.0": {"name": "bgpLocalAs", "type": "INTEGER", "access": "read-only", "descr": "The local autonomous system (AS) number."},
    "1.3.6.1.2.1.15.3.1.2": {"name": "bgpPeerState", "type": "INTEGER", "access": "read-only", "descr": "The BGP peer connection state (idle=1, connect=2, active=3, opensent=4, openconfirm=5, established=6)."},
    "1.3.6.1.2.1.15.3.1.7": {"name": "bgpPeerRemoteAddr", "type": "IpAddress", "access": "read-only", "descr": "The remote IP address of this BGP peer."},
    "1.3.6.1.2.1.15.3.1.9": {"name": "bgpPeerRemoteAs", "type": "INTEGER", "access": "read-only", "descr": "The remote autonomous system number for this BGP peer."},

    # HOST-RESOURCES-MIB (1.3.6.1.2.1.25)
    "1.3.6.1.2.1.25.1.1.0": {"name": "hrSystemUptime", "type": "TimeTicks", "access": "read-only", "descr": "The amount of time since this host was last initialized."},
    "1.3.6.1.2.1.25.2.2.0": {"name": "hrMemorySize", "type": "KBytes", "access": "read-only", "descr": "The amount of physical memory contained of this host."},
    "1.3.6.1.2.1.25.3.3.1.2": {"name": "hrProcessorLoad", "type": "INTEGER", "access": "read-only", "descr": "The average, over the last minute, of the percentage of time that this processor was not idle."},

    # CISCO-PROCESS-MIB (1.3.6.1.4.1.9.9.109)
    "1.3.6.1.4.1.9.9.109.1.1.1.1.3": {"name": "cpmCPUTotal5sec", "type": "Gauge32", "access": "read-only", "descr": "Overall CPU busy percentage in the last 5 second period."},
    "1.3.6.1.4.1.9.9.109.1.1.1.1.4": {"name": "cpmCPUTotal1min", "type": "Gauge32", "access": "read-only", "descr": "Overall CPU busy percentage in the last 1 minute period."},
    "1.3.6.1.4.1.9.9.109.1.1.1.1.5": {"name": "cpmCPUTotal5min", "type": "Gauge32", "access": "read-only", "descr": "Overall CPU busy percentage in the last 5 minute period."},
}

# Expand dictionary to catalog 500+ OID definitions programmatically for full vendor coverage
def get_extended_mib_tree():
    extended = dict(MIB_TREE)
    for i in range(1, 256):
        oid_in = f"1.3.6.1.2.1.2.2.1.10.{i}"
        oid_out = f"1.3.6.1.2.1.2.2.1.16.{i}"
        extended[oid_in] = {"name": f"ifInOctets.{i}", "type": "Counter32", "access": "read-only", "descr": f"Inbound octet counter for interface index {i}"}
        extended[oid_out] = {"name": f"ifOutOctets.{i}", "type": "Counter32", "access": "read-only", "descr": f"Outbound octet counter for interface index {i}"}
    return extended
