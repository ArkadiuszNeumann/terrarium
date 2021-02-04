from fastapi import APIRouter
from .schema import Settings as SettingsRequest
from .job import *

router = APIRouter()


@router.get("/")
def get_settings():
    return get_settings_from_db()


@router.get("/{type}")
def get_settings_by_sensor(type: str = None):
    return get_settings_from_db(type)


@router.post("/")
def add_settings_by_sensor(req: SettingsRequest):
    status = add_setting_to_db(req)
    return status

@router.patch("/")
def edit_settings_by_id(req: SettingsRequest):
    status = edit_setting_db(req)
    return status
