from .crud import *
from datetime import datetime
from app.routes.sensor.crud import get_sensors_by_attribute
from app.relay.schema import Relay
from app.utils.scheduler.scheduler import ScheduleTasks
import functools


def get_settings_from_db(sensor_type=None):
    try:
        if sensor_type is None:
            settings = get_all_settings()
            return settings
        else:
            sensors = get_sensors_by_attribute(attr='type', value=sensor_type)
            settings = get_settings_by_type(sensors)
            return settings
    except Exception:
        raise Exception


def add_setting_to_db(req, sensor):
    try:
        add_settings(req, sensor)
        return {"status": "ok"}
    except Exception:
        raise Exception


def edit_setting_db(req, sensor):
    try:
        edit_settings(req, sensor)
        return {"status": "ok"}
    except Exception:
        raise Exception
