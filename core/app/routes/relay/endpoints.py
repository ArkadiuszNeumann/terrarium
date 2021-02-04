from fastapi import APIRouter
from .schema import Relay
from .job import *
from typing import Optional, List

router = APIRouter()


@router.get("/", response_model=List[Relay])
def relay_get(start: Optional[str] = None, end: Optional[str] = None):
    return get_relay_from_db(start=start, end=end)


@router.get("/last", response_model=List[Relay])
def relay_get():
    return get_relay_from_db(last=True)


@router.get("/{sensor_id}", response_model=List[Relay])
def relay_get(sensor_id: int, start: Optional[str] = None, end: Optional[str] = None):
    return get_relay_from_db(sensor_id=sensor_id, start=start, end=end)


@router.get("/{sensor_id}/last", response_model=List[Relay])
def get_last_temperature(sensor_id: int):
    return get_relay_from_db(sensor_id, last=True)


@router.post("/{sensor_id}")
async def relay_action(sensor_id: int, req: Relay):
    return action(req, sensor_id)
