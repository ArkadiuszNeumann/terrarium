from app.utils.database.temperature import Temperature
from app.utils.database.base.base import session_factory
from app.utils.database.db_connection import *
from app.utils.database import pydantication
from .schema import TemperatureResponse
from datetime import datetime


def get_temperature(close_session=True, last=False, session=None):
    if session is None:
        session = session_factory()
    try:
        if last:
            temperature = select_newest_from_db(Temperature, False, session)
            response = pydantication.create_pydantic_object(temperature, TemperatureResponse)
            if close_session:
                session.close()
            return response

        else:
            list_temperature = []
            temperature = select_all_from_db(Temperature, False, session)
        if close_session:
            session.close()
        for obj in temperature:
            response = pydantication.create_pydantic_object(obj, TemperatureResponse)
            list_temperature.append(response)

        return list_temperature
    except Exception:
        raise ConnectionError


def get_temperature_start_end_date(start, end, close_session=True, session=None):
    if session is None:
        session = session_factory()
    attr = 'last_update'
    try:
        list_temperature = []
        temperature = select_query_from_db(Temperature, False, session).filter(getattr(Temperature, attr) <= end,
                                                                               getattr(Temperature, attr) >= start)
        if close_session:
            session.close()
        if not temperature:
            return []
        for obj in temperature:
            response = pydantication.create_pydantic_object(obj, TemperatureResponse)
            list_temperature.append(response)
        return list_temperature
    except Exception:
        raise ConnectionError


def add_temperature(req, sensor_id):
    try:
        response = pydantication.create_db_object(req, Temperature, skip=["id"], sensor_id=sensor_id,
                                                  last_update=int(datetime.timestamp(datetime.now())))
        insert_into_db(response)
    except:
        raise ConnectionError
