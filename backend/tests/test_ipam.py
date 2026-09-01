import pytest
from backend.services.ipam_service import IPAMService
from backend.schemas.ipam import SubnetCreate, IPAddressCreate
from backend.models.ipam import SubnetCategory, IPStatus

@pytest.mark.asyncio
async def test_subnet_creation_and_cidr_parsing(async_db):
    subnet_in = SubnetCreate(
        cidr="172.16.10.0/24",
        name="Server Test Farm",
        category=SubnetCategory.DATA_CENTER,
        gateway_ip="172.16.10.1",
        description="UnitTest Subnet Pool"
    )
    subnet = await IPAMService.create_subnet(async_db, subnet_in)
    assert subnet.id is not None
    assert subnet.cidr == "172.16.10.0/24"
    assert subnet.total_ips == 254

@pytest.mark.asyncio
async def test_ip_address_allocation(async_db):
    subnet_in = SubnetCreate(
        cidr="192.168.50.0/24",
        name="VoIP Test Net",
        category=SubnetCategory.VOIP,
        gateway_ip="192.168.50.1"
    )
    subnet = await IPAMService.create_subnet(async_db, subnet_in)

    ip_in = IPAddressCreate(
        subnet_id=subnet.id,
        ip_address="192.168.50.10",
        mac_address="00:11:22:33:AA:BB",
        hostname="sip-phone-101",
        status=IPStatus.ACTIVE,
        assigned_to="Engineering Desk"
    )
    ip_obj = await IPAMService.allocate_ip(async_db, ip_in)
    assert ip_obj.id is not None
    assert ip_obj.ip_address == "192.168.50.10"
    assert ip_obj.dns_ptr_record == "sip-phone-101.vortexnet.local"
