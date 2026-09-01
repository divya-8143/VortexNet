import csv
import io
from typing import Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.device_service import DeviceService
from backend.services.ipam_service import IPAMService
from backend.services.incident_service import IncidentService

class ReportService:
    @staticmethod
    async def generate_devices_csv(db: AsyncSession) -> str:
        devices = await DeviceService.get_all_devices(db)
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["ID", "Hostname", "Management IP", "Device Type", "Vendor", "Model", "Location", "Status", "CPU (%)", "RAM (%)"])
        for d in devices:
            writer.writerow([d.id, d.hostname, d.management_ip, d.device_type, d.vendor, d.model, d.location, d.status, d.cpu_usage_pct, d.ram_usage_pct])
        return output.getvalue()

    @staticmethod
    async def generate_ipam_csv(db: AsyncSession) -> str:
        subnets = await IPAMService.get_all_subnets(db)
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["ID", "CIDR", "Name", "Category", "Gateway IP", "Total IPs", "Used IPs", "Utilization (%)"])
        for s in subnets:
            writer.writerow([s.id, s.cidr, s.name, s.category, s.gateway_ip, s.total_ips, s.used_ips, s.utilization_pct])
        return output.getvalue()
