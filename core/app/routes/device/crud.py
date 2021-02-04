from app.utils.database.device import Device as DeviceDB
from app.utils.database.base.base import session_factory
from app.utils.database.db_connection import *
from app.utils.database import pydantication
from .schema import Device as Device_request
from datetime import datetime


def get_devices(close_session=True, session=None):
    if session is None:
        session = session_factory()
    try:
        device_list = []
        device = select_all_from_db(DeviceDB, False, session)
        if close_session:
            session.close()
            for obj in device:
                response = pydantication.create_pydantic_object(obj, Device_request)
                device_list.append(response)
    except Exception:
        raise ConnectionError
    return device_list


def get_device_by_id(dev_id, close_session=True, session=None):
    if session is None:
        session = session_factory()
    try:
        device = select_query_from_db(DeviceDB, False, session).filter(DeviceDB.id == dev_id)
        if close_session:
            session.close()
        if not device:
            return []
        for obj in device:
            response = pydantication.create_pydantic_object(obj, Device_request)
            return response
    except Exception:
        raise ConnectionError


def add_device(req):
    response = pydantication.create_db_object(req, DeviceDB, skip=["id"])
    insert_into_db(response)
    return


def delete_device(sensor_id, close_session=True, session=None):
    if session is None:
        session = session_factory()
    try:
        device = select_query_from_db(DeviceDB, False, session).filter(getattr(DeviceDB, 'id') == sensor_id).first()
        delete_from_db(device, True, session)
        if close_session:
            session.close()
        return
    except:
        raise ConnectionError