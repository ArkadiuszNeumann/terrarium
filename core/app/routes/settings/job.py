from .crud import *
from datetime import datetime
from app.routes.sensor.crud import get_sensors_by_attribute
from app.utils.scheduler.scheduler import ScheduleTasks
from app.routes.relay.job import action
from app.routes.relay.schema import Relay
from app.routes.temperature.schema import TemperatureRequest
from app.routes.humidity.schema import HumidityRequest
import functools
import logging

logger = logging.getLogger(__name__)


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


def add_setting_to_db(req):
    try:
        add_settings(req)
        sensor_type = get_sensors_by_attribute(attr='id', value=req.sensor_id)[0].type
        if sensor_type in 'relay':
            REQ = create_relay_object(req, sensor_type)
            scheduled_action(action, REQ, req.sensor_id, req.value)
        #   action(req, sensor_id, slot):
        #   scheduled_action(
        return {"status": "OK"}
    except Exception:
        raise Exception


def edit_setting_db(req):
    edit_settings(req)
    return {"status": "ok"}
    # try:
    #     edit_settings(req)
    #     return {"status": "ok"}
    # except Exception:
    #     raise Exception
    #


def scheduled_action(job, req, sensor_id, hour_minute):
    obj = ScheduleTasks()
    obj.add_job(functools.partial(job, req, sensor_id), hour_minute)
    return {"status": "D"}

def scheduled_delete():
    obj = ScheduleTasks()
    obj.remove_job()
    return {"status": "kllllll"}


def create_schema_object(sensor_type):
    switcher = {
        'relay': Relay,
        'temperature': TemperatureRequest,
        'humidity': HumidityRequest
    }
    return switcher.get(sensor_type, "Invalid sensor")


def decode_setting_key(key):
    if key == 'turn-on':
        return 1
    if key == 'turn-off':
        return 0
    else:
        return


def create_relay_object(req, sensor_type):
    obj = create_schema_object(sensor_type)
    logger.error(req)
    relay = obj()
    relay.device_id = req.device_id
    relay.sensor_id = req.sensor_id
    logger.error(obj)
    if obj is Relay:
        relay.status = decode_setting_key(req.key)
    return relay
