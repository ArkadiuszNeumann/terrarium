from fastapi import APIRouter
from .schema import Device
from .job import *
from typing import Optional, List

router = APIRouter()


@router.get("/", response_model=List[Device])
async def get_devices():
    return get_device_from_db()


@router.post("/")
async def add_new_device(req: Device):
    return add_device(req)


@router.delete("/{device_id}")
async def delete_device(device_id: int = None):
    return delete_device_from_db(device_id)
