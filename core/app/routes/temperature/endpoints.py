from fastapi import APIRouter
from .schema import *
from .job import get_temperature_from_db, add_temperature_to_db
from greenletio import await_
from typing import Optional, List

router = APIRouter()


@router.get("/temperature", response_model=List[TemperatureResponse])
def get_temperature(start: Optional[str] = None, end: Optional[str] = None, sensor: Optional[int] = None):
    return get_temperature_from_db(start, end, sensor)


@router.get("/temperature/last", response_model=TemperatureResponse)
def get_last_temperature(sensor: Optional[int] = None):
    return get_temperature_from_db(sensor, last=True)


@router.post("/temperature/{sensor_id}")
def add_new_temperature(sensor_id: int, req: TemperatureRequest):
    add_temperature_to_db(req, sensor_id)
    return {"STATUS": "OK"}
