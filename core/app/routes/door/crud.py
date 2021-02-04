from app.utils.database.door import Door
from app.utils.database.base.base import session_factory
from app.utils.database.db_connection import *
from app.utils.database import pydantication
from .schema import DoorResponse
from datetime import datetime


def get_door(close_session=True, last=False, session=None):
    if session is None:
        session = session_factory()
    try:
        if last:
            door = select_newest_from_db(Door, False, session)
            response = pydantication.create_pydantic_object(door, DoorResponse)
            if close_session:
                session.close()
            return response
        else:
            list_door = []
            door = select_all_from_db(Door, False, session)
        if close_session:
            session.close()
        for obj in door:
            response = pydantication.create_pydantic_object(obj, DoorResponse)
            list_door.append(response)
        return list_door
    except Exception:
        raise ConnectionError


def get_door_start_end_date(start, end, close_session=True, session=None):
    if session is None:
        session = session_factory()
    attr = 'last_update'
    try:
        list_door = []
        door = select_query_from_db(Door, False, session).filter(getattr(Door, attr) <= end,
                                                                 getattr(Door, attr) >= start)
        if close_session:
            session.close()
        if not door:
            return []
        for obj in door:
            response = pydantication.create_pydantic_object(obj, DoorResponse)
            list_door.append(response)
        return list_door
    except Exception:
        raise ConnectionError


def add_door(req, sensor_id):
    try:
        response = pydantication.create_db_object(req, Door, skip=["id"], sensor_id=sensor_id,
                                                  last_update=int(datetime.timestamp(datetime.now())))
        insert_into_db(response)
    except:
        raise ConnectionError
