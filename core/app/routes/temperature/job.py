from .crud import *
from datetime import datetime
from fastapi import HTTPException


logger = logging.getLogger(__name__)

def get_temperature_from_db(start=None, end=None, sensor=None, last=False):
    try:
        if last:
            return get_temperature(last=True)
        if start is None and end is None:
            temperature = get_temperature()
            return temperature
        if start is None:
            start = 0
        if end is None:
            end = int(datetime.timestamp(datetime.now()))
        temperature = get_temperature_start_end_date(start, end)
        return temperature
    except Exception:
        raise Exception


def add_temperature_to_db(req, sensor):
    try:
        if req.value == 0:
            raise HTTPException(status_code=400, detail="Wrong Value")
        add_temperature(req, sensor)
        return {"status": "ok"}
    except Exception:
        raise Exception

