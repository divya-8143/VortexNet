from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_db
from backend.schemas.device import DeviceOut, DeviceCreate, DeviceUpdate, DeviceSummary
from backend.services.device_service import DeviceService
from backend.api.deps import get_current_user

router = APIRouter()

@router.get("/", response_model=List[DeviceOut])
async def list_devices(
    device_type: Optional[str] = None,
    status: Optional[str] = None,
    db: AsyncSession = Depends(get_db),
    user = Depends(get_current_user)
):
    devices = await DeviceService.get_all_devices(db, device_type=device_type, status_filter=status)
    return [DeviceOut.model_validate(d) for d in devices]

@router.get("/summary", response_model=DeviceSummary)
async def get_summary(db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    return await DeviceService.get_device_summary(db)

@router.get("/{device_id}", response_model=DeviceOut)
async def get_device(device_id: int, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    device = await DeviceService.get_device_by_id(db, device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return DeviceOut.model_validate(device)

@router.post("/", response_model=DeviceOut)
async def create_device(device_in: DeviceCreate, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    device = await DeviceService.create_device(db, device_in)
    return DeviceOut.model_validate(device)

@router.put("/{device_id}", response_model=DeviceOut)
async def update_device(device_id: int, device_in: DeviceUpdate, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    device = await DeviceService.update_device(db, device_id, device_in)
    return DeviceOut.model_validate(device)

@router.delete("/{device_id}")
async def delete_device(device_id: int, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    await DeviceService.delete_device(db, device_id)
    return {"message": "Device deleted successfully"}
