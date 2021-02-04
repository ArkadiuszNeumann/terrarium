from .crud import *
from datetime import datetime


def get_humidity_from_db(start=None, end=None, sensor=None, last=False):
    try:
        if last:
            return get_humidity(last=True)
        if start is None and end is None:
            humidity = get_humidity()
            return humidity
        if start is None:
            start = 0
        if end is None:
            end = int(datetime.timestamp(datetime.now()))
        humidity = get_humidity_start_end_date(start, end)
        return humidity
    except Exception:
        raise Exception



def add_humidity_to_db(req, sensor):
    try:

        add_humidity(req, sensor)
        return {"status": "ok"}
    except Exception:
        raise Exception
