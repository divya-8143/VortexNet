from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_db
from backend.services.report_service import ReportService
from backend.api.deps import get_current_user

router = APIRouter()

@router.get("/export/devices/csv")
async def export_devices_csv(db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    csv_data = await ReportService.generate_devices_csv(db)
    return Response(content=csv_data, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=vortexnet_devices.csv"})

@router.get("/export/ipam/csv")
async def export_ipam_csv(db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    csv_data = await ReportService.generate_ipam_csv(db)
    return Response(content=csv_data, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=vortexnet_ipam.csv"})
