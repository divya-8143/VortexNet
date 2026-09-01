export type DeviceType = 'ROUTER' | 'SWITCH' | 'FIREWALL' | 'ACCESS_POINT' | 'SERVER' | 'LOAD_BALANCER';
export type DeviceStatus = 'ONLINE' | 'OFFLINE' | 'WARNING' | 'CRITICAL' | 'MAINTENANCE';
export type VendorType = 'CISCO' | 'JUNIPER' | 'ARISTA' | 'PALO_ALTO' | 'FORTINET' | 'ARUBA' | 'LINUX';

export interface Device {
  id: number;
  hostname: str;
  management_ip: str;
  mac_address: str;
  device_type: DeviceType;
  vendor: VendorType;
  model: str;
  firmware_version: str;
  serial_number: str;
  location: str;
  status: DeviceStatus;
  cpu_usage_pct: number;
  ram_usage_pct: number;
  temperature_celsius: number;
  uptime_seconds: number;
  created_at: str;
}

export interface DeviceSummary {
  total_devices: number;
  online_count: number;
  offline_count: number;
  warning_count: number;
  critical_count: number;
  avg_cpu_pct: number;
  avg_ram_pct: number;
}

export interface Subnet {
  id: number;
  cidr: str;
  name: str;
  vlan_id?: number;
  category: str;
  gateway_ip?: str;
  description?: str;
  total_ips: number;
  used_ips: number;
  utilization_pct: number;
}

export interface Incident {
  id: number;
  title: str;
  device_id: number;
  severity: 'CRITICAL' | 'MAJOR' | 'MINOR' | 'WARNING' | 'INFO';
  status: 'TRIGGERED' | 'ACKNOWLEDGED' | 'IN_PROGRESS' | 'RESOLVED' | 'CLOSED';
  description: str;
  assigned_to: str;
  triggered_at: str;
}

export interface Syslog {
  id: number;
  hostname: str;
  facility: str;
  severity: str;
  message: str;
  timestamp: str;
}

export interface User {
  id: number;
  username: str;
  email: str;
  full_name: str;
  role: 'SUPER_ADMIN' | 'NETWORK_ENGINEER' | 'NOC_OPERATOR' | 'READ_ONLY_VIEWER';
  department: str;
  is_active: boolean;
}
