from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_db
from backend.schemas.ipam import SubnetOut, SubnetCreate, IPAddressOut, IPAddressCreate
from backend.services.ipam_service import IPAMService
from backend.api.deps import get_current_user

router = APIRouter()

@router.get("/subnets", response_model=List[SubnetOut])
async def list_subnets(db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    return await IPAMService.get_all_subnets(db)

@router.post("/subnets", response_model=SubnetOut)
async def create_subnet(subnet_in: SubnetCreate, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    subnet = await IPAMService.create_subnet(db, subnet_in)
    return SubnetOut(
        id=subnet.id, cidr=subnet.cidr, name=subnet.name, vlan_id=subnet.vlan_id,
        category=subnet.category, gateway_ip=subnet.gateway_ip, description=subnet.description,
        total_ips=subnet.total_ips, used_ips=0, utilization_pct=0.0
    )

@router.get("/subnets/{subnet_id}/addresses", response_model=List[IPAddressOut])
async def get_subnet_addresses(subnet_id: int, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    addresses = await IPAMService.get_subnet_addresses(db, subnet_id)
    return [IPAddressOut.model_validate(a) for a in addresses]

@router.post("/addresses", response_model=IPAddressOut)
async def allocate_ip(ip_in: IPAddressCreate, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    ip = await IPAMService.allocate_ip(db, ip_in)
    return IPAddressOut.model_validate(ip)
