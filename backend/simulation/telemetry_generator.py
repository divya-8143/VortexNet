import asyncio
import logging
from sqlalchemy.future import select
from backend.database import AsyncSessionLocal
from backend.models.device import NetworkDevice, DeviceStatus
from backend.simulation.snmp_simulator import SNMPSimulator
from backend.simulation.syslog_simulator import SyslogSimulator
from backend.models.syslog import SyslogEntry, SyslogSeverity, SyslogFacility

logger = logging.getLogger("vortexnet.simulation")

class TelemetryGenerator:
    """
    Background simulation worker that updates device telemetry and emits synthetic syslogs
    """
    
    @staticmethod
    async def run_telemetry_tick():
        async with AsyncSessionLocal() as db:
            try:
                res = await db.execute(select(NetworkDevice))
                devices = res.scalars().all()
                if not devices:
                    return

                for dev in devices:
                    if dev.status == DeviceStatus.OFFLINE:
                        continue

                    # SNMP poll telemetry simulation
                    snmp_data = SNMPSimulator.get_snmp_telemetry(
                        hostname=dev.hostname,
                        vendor=dev.vendor.value if hasattr(dev.vendor, 'value') else str(dev.vendor),
                        current_cpu=dev.cpu_usage_pct,
                        current_ram=dev.ram_usage_pct
                    )

                    dev.cpu_usage_pct = snmp_data["cpu_usage_pct"]
                    dev.ram_usage_pct = snmp_data["ram_usage_pct"]
                    dev.temperature_celsius = snmp_data["temperature_celsius"]
                    dev.uptime_seconds += 5

                    # Auto update status based on CPU/RAM thresholds
                    if dev.cpu_usage_pct > 90.0 or dev.ram_usage_pct > 92.0:
                        dev.status = DeviceStatus.CRITICAL
                    elif dev.cpu_usage_pct > 80.0 or dev.ram_usage_pct > 85.0:
                        dev.status = DeviceStatus.WARNING
                    else:
                        dev.status = DeviceStatus.ONLINE

                await db.commit()
            except Exception as e:
                logger.error(f"Telemetry simulation tick error: {str(e)}")
                await db.rollback()
