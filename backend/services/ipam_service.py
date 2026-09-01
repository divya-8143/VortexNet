import ipaddress
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from backend.models.ipam import Subnet, IPAddress, IPStatus
from backend.schemas.ipam import SubnetCreate, IPAddressCreate, IPAddressUpdate, SubnetOut

class IPAMService:
    @staticmethod
    async def get_all_subnets(db: AsyncSession) -> List[SubnetOut]:
        result = await db.execute(select(Subnet).order_by(Subnet.cidr.asc()))
        subnets = result.scalars().all()
        out = []
        for s in subnets:
            pct = round((s.used_ips / max(s.total_ips, 1)) * 100.0, 1)
            out.append(SubnetOut(
                id=s.id,
                cidr=s.cidr,
                name=s.name,
                vlan_id=s.vlan_id,
                category=s.category,
                gateway_ip=s.gateway_ip,
                description=s.description,
                total_ips=s.total_ips,
                used_ips=s.used_ips,
                utilization_pct=pct
            ))
        return out

    @staticmethod
    async def create_subnet(db: AsyncSession, subnet_in: SubnetCreate) -> Subnet:
        try:
            network = ipaddress.ip_network(subnet_in.cidr, strict=False)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid CIDR string: {str(e)}")

        existing = await db.execute(select(Subnet).where(Subnet.cidr == str(network)))
        if existing.scalars().first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Subnet {network} already exists.")

        total_ips = max(network.num_addresses - 2, 1)
        subnet = Subnet(
            cidr=str(network),
            name=subnet_in.name,
            vlan_id=subnet_in.vlan_id,
            category=subnet_in.category,
            gateway_ip=subnet_in.gateway_ip or str(network.network_address + 1),
            description=subnet_in.description,
            total_ips=total_ips,
            used_ips=0
        )
        db.add(subnet)
        await db.commit()
        await db.refresh(subnet)
        return subnet

    @staticmethod
    async def get_subnet_addresses(db: AsyncSession, subnet_id: int) -> List[IPAddress]:
        result = await db.execute(select(IPAddress).where(IPAddress.subnet_id == subnet_id).order_by(IPAddress.ip_address.asc()))
        return list(result.scalars().all())

    @staticmethod
    async def allocate_ip(db: AsyncSession, ip_in: IPAddressCreate) -> IPAddress:
        existing = await db.execute(select(IPAddress).where(IPAddress.ip_address == ip_in.ip_address))
        if existing.scalars().first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"IP Address {ip_in.ip_address} is already recorded.")

        subnet_res = await db.execute(select(Subnet).where(Subnet.id == ip_in.subnet_id))
        subnet = subnet_res.scalars().first()
        if not subnet:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Subnet ID {ip_in.subnet_id} not found.")

        ip_obj = IPAddress(**ip_in.model_dump())
        if not ip_obj.dns_ptr_record and ip_obj.hostname:
            ip_obj.dns_ptr_record = f"{ip_obj.hostname}.vortexnet.local"

        db.add(ip_obj)
        if ip_obj.status in [IPStatus.ACTIVE, IPStatus.RESERVED, IPStatus.DHCP_LEASE]:
            subnet.used_ips += 1

        await db.commit()
        await db.refresh(ip_obj)
        return ip_obj
