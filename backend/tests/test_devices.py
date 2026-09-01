import pytest
from backend.services.device_service import DeviceService
from backend.schemas.device import DeviceCreate, DeviceUpdate
from backend.models.device import DeviceType, VendorType, DeviceStatus

@pytest.mark.asyncio
async def test_create_and_get_network_device(async_db):
    device_in = DeviceCreate(
        hostname="core-router-test-01",
        management_ip="10.255.0.1",
        mac_address="00:11:22:33:44:55",
        device_type=DeviceType.ROUTER,
        vendor=VendorType.CISCO,
        model="ASR-1001-X",
        firmware_version="17.3.4",
        serial_number="SN-TEST-9999",
        location="Lab Test Bench"
    )
    device = await DeviceService.create_device(async_db, device_in)
    assert device.id is not None
    assert device.hostname == "core-router-test-01"
    assert device.status == DeviceStatus.ONLINE

    fetched = await DeviceService.get_device_by_id(async_db, device.id)
    assert fetched is not None
    assert fetched.management_ip == "10.255.0.1"

@pytest.mark.asyncio
async def test_update_device_status(async_db):
    device_in = DeviceCreate(
        hostname="dist-switch-test-01",
        management_ip="10.255.0.2",
        mac_address="00:11:22:33:44:56",
        device_type=DeviceType.SWITCH,
        vendor=VendorType.ARISTA,
        model="7050X3",
        firmware_version="4.25",
        serial_number="SN-TEST-8888",
        location="Lab Test Bench"
    )
    device = await DeviceService.create_device(async_db, device_in)
    
    updated = await DeviceService.update_device(async_db, device.id, DeviceUpdate(status=DeviceStatus.WARNING))
    assert updated.status == DeviceStatus.WARNING
