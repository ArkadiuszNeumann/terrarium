from fastapi import APIRouter
from .schema import *
from .job import get_door_from_db, add_door_to_db
from greenletio import await_
from typing import Optional, List

router = APIRouter()


@router.get("/door", response_model=List[DoorResponse])
async def get_status(start: Optional[str] = None, end: Optional[str] = None):
    return get_door_from_db(start, end)


@router.get("/door/last", response_model=DoorResponse)
async def get_status():
    return get_door_from_db(last=True)


@router.post("/door/{sensor_id}")
async def add_door_status(sensor_id: int, req: DoorRequest):
    await_(add_door_to_db(req, sensor_id))
    return {"STATUS": "OK"}

