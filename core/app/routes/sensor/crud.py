from app.utils.database.sensor import Sensor
from app.utils.database.base.base import session_factory
from app.utils.database.db_connection import *
from app.utils.database import pydantication
from .schema import Sensor as SersorRequest
import logging
logger = logging.getLogger(__name__)

def get_all_sensors(close_session=True, session=None):
    if session is None:
        session = session_factory()
    try:
        list_sensors = []
        sensors = select_all_from_db(Sensor, False, session)
        if close_session:
            session.close()
        for obj in sensors:
            response = pydantication.create_pydantic_object(obj, SersorRequest)
            list_sensors.append(response)
        return list_sensors
    except Exception:
        raise ConnectionError


def get_sensors_by_attribute(attr, value, close_session=True, session=None):
    if session is None:
        session = session_factory()
    try:
        list_sensors = []
        sensors = select_query_from_db(Sensor, False, session).filter(getattr(Sensor, attr) == value)
        if close_session:
            session.close()
        for obj in sensors:
            response = pydantication.create_pydantic_object(obj, SersorRequest)
            list_sensors.append(response)
        return list_sensors
    except Exception:
        raise ConnectionError


def add_sensor(type):
    try:
        # response = pydantication.create_db_object(req, Sensor, skip=["id"])
        sensor = Sensor()
        sensor.type = type
        return insert_into_db(sensor)
    except:
        raise ConnectionError


def delete_sensor(sensor_id, close_session=True, session=None):
    if session is None:
        session = session_factory()
    try:
        sensors = select_query_from_db(Sensor, False, session).filter(getattr(Sensor, 'id') == sensor_id).first()
        delete_from_db(sensors, True, session)
        if close_session:
            session.close()
        return
    except:
        raise ConnectionError

