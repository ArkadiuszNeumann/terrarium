from fastapi import APIRouter
from .schema import *
from .job import get_humidity_from_db, add_humidity_to_db
from greenletio import await_
from typing import Optional, List

router = APIRouter()


@router.get("/humidity", response_model=List[HumidityResponse])
def get_humidity(start: Optional[str] = None, end: Optional[str] = None, sensor_id: Optional[int] = None):
    return get_humidity_from_db(start, end)


@router.get("/humidity/last", response_model=HumidityResponse)
def get_humidity(sensor: Optional[int] = None):
    return get_humidity_from_db(sensor, last=True)


@router.post("/humidity/{sensor_id}")
async def add_new_humidity(sensor_id: int, req: HumidityRequest):
    await_(add_humidity_to_db(req, sensor_id))
    return {"STATUS": "OK"}
