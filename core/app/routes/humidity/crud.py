from app.utils.database.humidity import Humidity
from app.utils.database.base.base import session_factory
from app.utils.database.db_connection import *
from app.utils.database import pydantication
from .schema import HumidityResponse
from datetime import datetime


def get_humidity(close_session=True, last=False, session=None):
    if session is None:
        session = session_factory()
    try:

        if last:
            humidity = select_newest_from_db(Humidity, False, session)
            response = pydantication.create_pydantic_object(humidity, HumidityResponse)
            if close_session:
                session.close()
            return response
        else:
            list_humidity = []
            humidity = select_all_from_db(Humidity, False, session)
        if close_session:
            session.close()
        for obj in humidity:
            response = pydantication.create_pydantic_object(obj, HumidityResponse)
            list_humidity.append(response)
        return list_humidity
    except Exception:
        raise ConnectionError


def get_humidity_start_end_date(start, end, close_session=True, session=None):
    if session is None:
        session = session_factory()
    attr = 'last_update'
    try:
        list_humidity = []
        humidity = select_query_from_db(Humidity, False, session).filter(getattr(Humidity, attr) <= end,
                                                                         getattr(Humidity, attr) >= start)
        if close_session:
            session.close()
        if not humidity:
            return []
        for obj in humidity:
            response = pydantication.create_pydantic_object(obj, HumidityResponse)
            list_humidity.append(response)
        return list_humidity
    except Exception:
        raise ConnectionError


def add_humidity(req, sensor_id):
    try:
        response = pydantication.create_db_object(req, Humidity, skip=["id"], sensor_id=sensor_id, last_update=int(datetime.timestamp(datetime.now())))
        insert_into_db(response)
    except:
        raise ConnectionError
