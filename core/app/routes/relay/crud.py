from app.utils.database.db_connection import *
from app.utils.database.relay import Relay as RelayDB
from .schema import Relay
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def add_relay_status(req, sensor_id):
    try:
        response = pydantication.create_db_object(req, RelayDB, skip=["id"], sensor_id=sensor_id,
                                                  last_update=int(datetime.timestamp(datetime.now())))
        insert_into_db(response)
    except Exception:
        raise ConnectionError


def get_relay_by_senor_id(sensor_id, close_session=True, session=None, last=False):
    if session is None:
        session = session_factory()
    list_relays = []
    try:
        if last:
            relay = select_query_from_db(RelayDB, False, session).filter(RelayDB.sensor_id == sensor_id).order_by(
                RelayDB.id.desc()).first()
            response = pydantication.create_pydantic_object(relay, Relay)
            list_relays.append(response)
        else:
            relay = select_query_from_db(RelayDB, False, session).filter(RelayDB.sensor_id == sensor_id)
            for obj in relay:
                response = pydantication.create_pydantic_object(obj, Relay)
                list_relays.append(response)
        if close_session:
            session.close()
        return list_relays
    except TypeError:
        return []
    except Exception:
        raise ConnectionError


def get_all_relay(close_session=True, session=None, last=False):
    if session is None:
        session = session_factory()
    list_relays = []
    try:
        if last:
            relay = select_newest_from_db(RelayDB, False, session)
            response = pydantication.create_pydantic_object(relay, Relay)
            list_relays.append(response)
        else:
            relay = select_all_from_db(RelayDB, False, session)
            for obj in relay:
                response = pydantication.create_pydantic_object(obj, Relay)
                list_relays.append(response)
        if close_session:
            session.close()
        return list_relays
    except TypeError:
        return []
    except Exception:
        raise ConnectionError


def get_relay_start_end_date(start, end, sensor_id=None, close_session=True, session=None):
    if session is None:
        session = session_factory()
    attr = 'last_update'
    try:
        list_relay = []
        if sensor_id is None:
            relay = select_query_from_db(RelayDB, False, session).filter(getattr(RelayDB, attr) <= end,
                                                                         getattr(RelayDB, attr) >= start)
            logger.error(relay)
        else:
            relay = select_query_from_db(RelayDB, False, session).filter(getattr(RelayDB, attr) <= end,
                                                                         getattr(RelayDB, attr) >= start,
                                                                         getattr(RelayDB, 'sensor_id') == sensor_id)
            logger.error(relay)
        if close_session:
            session.close()
        if not relay:
            return []
        for obj in relay:
            response = pydantication.create_pydantic_object(obj, Relay)
            list_relay.append(response)
        return list_relay
    except Exception:
        raise ConnectionError
