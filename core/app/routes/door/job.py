from .crud import *
from datetime import datetime


def get_door_from_db(start=None, end=None, last=False):
    try:
        if last:
            return get_door(last=True)
        if start is None and end is None:
            door = get_door()
            return door
        if start is None:
            start = 0
        if end is None:
            end = datetime.timestamp(datetime.now())
        door = get_door_start_end_date(start, end)
        return door
    except Exception:
        raise Exception


def add_door_to_db(req, sensor_id):
    try:
        add_door(req, sensor_id)
        return {"status": "ok"}
    except Exception:
        raise Exception
