from .crud import *
from datetime import datetime


def get_sensor_from_db(sensor_type=None):
    try:
        if sensor_type is None:
            sensors = get_all_sensors()
            return sensors
        else:
            sensors = get_sensors_by_attribute(attr='type', value=sensor_type)
            return sensors
    except Exception:
        raise Exception


def add_sensor_to_db(type):
    try:
        id = add_sensor(type)
        return {"id": id }
    except Exception:
        raise Exception

def delete_sensor_from_db(sensor_id):
    try:
        delete_sensor(sensor_id)
        return {"status": "ok"}
    except Exception:
        raise Exception
