from fastapi import APIRouter
from .schema import *
from .job import get_sensor_from_db, add_sensor_to_db, delete_sensor_from_db
from greenletio import await_
from typing import Optional, List

router = APIRouter()


@router.get("/", response_model=List[Sensor])
def get_sensor():
    return get_sensor_from_db()


@router.get("/{type}", response_model=List[Sensor])
def get_sensor(type: str = None):
    return get_sensor_from_db(type)


@router.post("/{type}")
def add_new_sensor(type: str = None):
    return add_sensor_to_db(type)

@router.delete("/{sensor_id}")
async def delete_sensor(sensor_id: int = None):
    await_(delete_sensor_from_db(sensor_id))
    return {"STATUS": "OK"}
