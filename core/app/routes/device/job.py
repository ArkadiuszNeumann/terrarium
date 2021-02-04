from .crud import *
from datetime import datetime


def get_device_from_db():
    try:
        humidity = get_devices()
        return humidity
    except Exception:
        raise Exception


def add_device_to_db(req):
    try:
        add_device(req)
        return {"status": "ok"}
    except Exception:
        raise Exception


def delete_device_from_db(sensor_id):
    try:
        delete_device(sensor_id)
        return {"status": "ok"}
    except Exception:
        raise Exception
