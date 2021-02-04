from .crud import *
from requests import post
from app.routes.device.crud import get_device_by_id, get_devices
from datetime import datetime


def get_relay_from_db(sensor_id=None, start=None, end=None, last=False):
    try:
        if sensor_id:
            if last:
                return get_relay_by_senor_id(sensor_id, last=True)
            if start is None and end is None:
                return get_relay_by_senor_id(sensor_id)
            if start is None:
                start = 0
            if end is None:
                end = int(datetime.timestamp(datetime.now()))
            return get_relay_start_end_date(start, end, sensor_id)
        else:
            if last:
                return get_all_relay(last=True)
            if start is None and end is None:
                return get_all_relay()
            if start is None:
                start = 0
            if end is None:
                end = int(datetime.timestamp(datetime.now()))
            return get_relay_start_end_date(start, end)
    except Exception:
        raise Exception


def action(req, sensor_id):
    try:
        dev_IP = get_device_by_id(req.device_id).ip
        url = f"http://{dev_IP}/relay/{sensor_id - 1}"
        response = post(url, json=req.__dict__)
        if response.status_code == 200:
            add_relay_status(req, sensor_id)
        else:
            raise ConnectionError
        return {"status": "ok"}
    except Exception:
        raise Exception


