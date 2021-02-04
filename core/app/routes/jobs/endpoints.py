from fastapi import APIRouter
from .schema import *
from .job import *
from greenletio import await_
from typing import Optional, List
import logging

router = APIRouter()


@router.get("/")
def get_settings():
    return get_settings_from_db()


@router.get("/{type}")
def get_sensor(type: str = None):
    print("kolorowanki")
    return get_settings_from_db(type)

#
# @router.post("/")
# async def add_new_sensor(req: Settings):
#     await_(add_setting_to_db(req))
#     return {"STATUS": "OK"}

@router.put("scheduler/{sensor_type}")
def add_scheduled_tasks():
    pass