import asyncio
import random
from sqlalchemy.future import select
from backend.database import sync_engine, Base, SyncSessionLocal
from backend.models.user import User, UserRole
from backend.models.device import NetworkDevice, DeviceType, DeviceStatus, VendorType
from backend.models.interface import DeviceInterface, InterfaceType, InterfaceStatus
from backend.models.vlan import VlanConfig
from backend.models.route import RoutingTableEntry, RouteProtocol, ArpEntry
from backend.models.ipam import Subnet, IPAddress, IPStatus, SubnetCategory
from backend.models.topology import TopologyLink, LinkType, LinkStatus
from backend.models.alert import AlertRule, MetricType, AlertSeverity
from backend.models.incident import Incident, IncidentStatus
from backend.models.syslog import SyslogEntry, SyslogSeverity, SyslogFacility
from backend.models.traffic import NetFlowRecord
from backend.security import get_password_hash

def seed_database():
    Base.metadata.create_all(bind=sync_engine)
    db = SyncSessionLocal()

    try:
        # 1. Seed Users
        if not db.query(User).first():
            print("Seeding default RBAC users...")
            admin = User(
                username="admin",
                email="admin@vortexnet.local",
                full_name="NetOps Administrator",
                hashed_password=get_password_hash("admin123"),
                role=UserRole.SUPER_ADMIN,
                is_superuser=True,
                department="Network Operations Center"
            )
            engineer = User(
                username="engineer",
                email="engineer@vortexnet.local",
                full_name="Lead Network Architect",
                hashed_password=get_password_hash("eng123"),
                role=UserRole.NETWORK_ENGINEER,
                department="Infrastructure Team"
            )
            operator = User(
                username="operator",
                email="operator@vortexnet.local",
                full_name="NOC Duty Shift 1",
                hashed_password=get_password_hash("op123"),
                role=UserRole.NOC_OPERATOR,
                department="NOC Operations"
            )
            db.add_all([admin, engineer, operator])
            db.commit()

        # 2. Seed Devices
        if not db.query(NetworkDevice).first():
            print("Seeding synthetic network devices...")
            devices_data = [
                ("core-router-01", "10.0.0.1", "00:1A:2B:3C:4D:01", DeviceType.ROUTER, VendorType.CISCO, "ASR 9000", "7.5.2", "Data Center Alpha - Rack A1"),
                ("core-router-02", "10.0.0.2", "00:1A:2B:3C:4D:02", DeviceType.ROUTER, VendorType.JUNIPER, "MX480", "21.4R1", "Data Center Alpha - Rack A2"),
                ("dist-switch-01", "10.0.0.11", "00:1A:2B:3C:4D:11", DeviceType.SWITCH, VendorType.CISCO, "Nexus 9300", "9.3.8", "Distribution Row 1"),
                ("dist-switch-02", "10.0.0.12", "00:1A:2B:3C:4D:12", DeviceType.ARISTA, "7050X3", "4.26.1F", "Distribution Row 2"),
                ("edge-firewall-01", "10.0.0.254", "00:1A:2B:3C:4D:FE", DeviceType.FIREWALL, VendorType.PALO_ALTO, "PA-5250", "10.1.4", "DMZ Gateway Perimeter"),
                ("access-switch-101", "10.0.1.10", "00:1A:2B:3C:4D:A1", DeviceType.SWITCH, VendorType.ARUBA, "CX 6300", "10.08", "Floor 1 MDF Closet"),
                ("wlc-primary-01", "10.0.0.50", "00:1A:2B:3C:4D:C1", DeviceType.ACCESS_POINT, VendorType.CISCO, "Catalyst 9800", "17.6.1", "Core Wireless Controller")
            ]

            dev_objs = []
            for hostname, ip, mac, dev_type, vendor, model, fw, loc in devices_data:
                dev = NetworkDevice(
                    hostname=hostname,
                    management_ip=ip,
                    mac_address=mac,
                    device_type=dev_type,
                    vendor=vendor,
                    model=model,
                    firmware_version=fw,
                    serial_number=f"SN-{random.randint(100000, 999999)}",
                    location=loc,
                    status=DeviceStatus.ONLINE,
                    cpu_usage_pct=round(random.uniform(12.0, 48.0), 1),
                    ram_usage_pct=round(random.uniform(25.0, 62.0), 1),
                    temperature_celsius=round(random.uniform(34.0, 44.0), 1)
                )
                db.add(dev)
                dev_objs.append(dev)
            db.commit()

            # Seed Interfaces for each device
            for dev in db.query(NetworkDevice).all():
                if_names = ["GigabitEthernet0/0/1", "GigabitEthernet0/0/2", "TenGigabitEthernet1/0/1", "TenGigabitEthernet1/0/2"]
                for i, name in enumerate(if_names):
                    iface = DeviceInterface(
                        device_id=dev.id,
                        name=name,
                        interface_type=InterfaceType.TEN_GIGABIT if "Ten" in name else InterfaceType.GIGABIT_ETHERNET,
                        status=InterfaceStatus.UP,
                        mac_address=f"00:1A:2B:{dev.id:02X}:{i:02X}:01",
                        ip_address=f"10.0.{dev.id}.{i+1}",
                        subnet_mask="255.255.255.0",
                        rx_bytes=random.randint(1000000, 500000000),
                        tx_bytes=random.randint(1000000, 400000000)
                    )
                    db.add(iface)
            db.commit()

        # 3. Seed Topology Links
        if not db.query(TopologyLink).first():
            print("Seeding network topology links...")
            devs = db.query(NetworkDevice).all()
            if len(devs) >= 4:
                link1 = TopologyLink(source_device_id=devs[0].id, source_interface="TenGigabitEthernet1/0/1", target_device_id=devs[1].id, target_interface="TenGigabitEthernet1/0/1", link_type=LinkType.TRUNK, capacity_gbps=100.0, status=LinkStatus.HEALTHY)
                link2 = TopologyLink(source_device_id=devs[0].id, source_interface="GigabitEthernet0/0/1", target_device_id=devs[2].id, target_interface="GigabitEthernet0/0/1", link_type=LinkType.TRUNK, capacity_gbps=10.0, status=LinkStatus.HEALTHY)
                link3 = TopologyLink(source_device_id=devs[1].id, source_interface="GigabitEthernet0/0/2", target_device_id=devs[3].id, target_interface="GigabitEthernet0/0/1", link_type=LinkType.TRUNK, capacity_gbps=10.0, status=LinkStatus.HEALTHY)
                link4 = TopologyLink(source_device_id=devs[2].id, source_interface="GigabitEthernet0/0/2", target_device_id=devs[4].id, target_interface="eth0", link_type=LinkType.WAN, capacity_gbps=1.0, status=LinkStatus.HEALTHY)
                db.add_all([link1, link2, link3, link4])
                db.commit()

        # 4. Seed IPAM Subnets
        if not db.query(Subnet).first():
            print("Seeding IPAM Subnets and Allocations...")
            s1 = Subnet(cidr="10.0.0.0/24", name="Core Infrastructure Management", category=SubnetCategory.MANAGEMENT, gateway_ip="10.0.0.1", total_ips=254, used_ips=15)
            s2 = Subnet(cidr="10.0.1.0/24", name="Data Center Server Subnet A", category=SubnetCategory.DATA_CENTER, gateway_ip="10.0.1.1", total_ips=254, used_ips=42)
            s3 = Subnet(cidr="10.0.10.0/24", name="Enterprise VoIP Network", category=SubnetCategory.VOIP, gateway_ip="10.0.10.1", total_ips=254, used_ips=88)
            db.add_all([s1, s2, s3])
            db.commit()

        # 5. Seed Alert Rules & Incidents
        if not db.query(AlertRule).first():
            print("Seeding Alert Rules & Initial Incidents...")
            r1 = AlertRule(rule_name="High CPU Utilization (>85%)", metric_type=MetricType.CPU_USAGE, threshold_value=85.0, severity=AlertSeverity.CRITICAL, description="Triggers critical alert when CPU spikes above 85%")
            r2 = AlertRule(rule_name="RAM Memory Exhaustion (>90%)", metric_type=MetricType.RAM_USAGE, threshold_value=90.0, severity=AlertSeverity.CRITICAL, description="Triggers alert when RAM is depleted")
            r3 = AlertRule(rule_name="Chassis Overheating (>65C)", metric_type=MetricType.TEMPERATURE, threshold_value=65.0, severity=AlertSeverity.MAJOR, description="Temperature threshold warning")
            db.add_all([r1, r2, r3])
            db.commit()

            dev = db.query(NetworkDevice).first()
            if dev:
                inc = Incident(title="BGP Peer Session Flapping on Edge Gateway", device_id=dev.id, severity=AlertSeverity.CRITICAL, status=IncidentStatus.TRIGGERED, description="Border Gateway Protocol neighbor session state changed from ESTABLISHED to ACTIVE/IDLE repeatedly.", assigned_to="Lead Network Architect")
                db.add(inc)
                db.commit()

        print("Database seed completed successfully!")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
