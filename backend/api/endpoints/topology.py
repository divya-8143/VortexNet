from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database import get_db
from backend.schemas.topology import TopologyGraphData, LinkOut, LinkCreate
from backend.services.topology_service import TopologyService
from backend.api.deps import get_current_user

router = APIRouter()

@router.get("/graph", response_model=TopologyGraphData)
async def get_topology_graph(db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    return await TopologyService.get_topology_graph(db)

@router.post("/links", response_model=LinkOut)
async def create_topology_link(link_in: LinkCreate, db: AsyncSession = Depends(get_db), user = Depends(get_current_user)):
    link = await TopologyService.create_link(db, link_in)
    return LinkOut.model_validate(link)
