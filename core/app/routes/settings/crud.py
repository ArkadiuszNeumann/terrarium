from app.utils.database.settings import Settings
from app.utils.database.base.base import session_factory
from app.utils.database.db_connection import *
from app.utils.database import pydantication
from .schema import Settings as SettingsRequest
from app.routes.sensor.crud import get_sensors_by_attribute
import sqlalchemy.orm.query
import logging

logger = logging.getLogger(__name__)


def get_all_settings(close_session=True, session=None):
    if session is None:
        session = session_factory()
    try:
        list_settings = []
        settings = select_all_from_db(Settings, False, session)
        if close_session:
            session.close()
        for obj in settings:
            response = pydantication.create_pydantic_object(obj, SettingsRequest)
            list_settings.append(response)
        return list_settings
    except Exception:
        raise ConnectionError


def get_settings_by_type(sensors=[], close_session=True, session=None):
    if session is None:
        session = session_factory()
    attr = 'sensor_id'
    try:
        list_sensors = []
        for sensor in sensors:
            list_sensors.append(sensor.id)
        list_settings = []
        settings = select_query_from_db(Settings, False, session).filter(Settings.sensor_id.in_(list_sensors))
        if close_session:
            session.close()
        for obj in settings:
            response = pydantication.edit_db_object(obj, SettingsRequest)
            list_settings.append(response)
        return list_settings
    except Exception:
        raise ConnectionError


def add_settings(req):
    try:
        response = pydantication.create_db_object(req, Settings, skip=["id"])
        insert_into_db(response)
    except:
        raise ConnectionError


def get_setting_by_id(setting_id, close_session=True, session=None):
    if session is None:
        session = session_factory()
    setting = select_query_from_db(Settings, False, session).filter(Settings.id == setting_id)
    if close_session:
        session.close()
    return setting


def edit_settings(req, session=None):
    #
    if session is None:
        session = session_factory()
    setting = get_setting_by_id(req.id, False, session).first()
    db = pydantication.create_db_object(req, Settings).__dict__
    logger.error(db)
    update_row(setting, db, True, session)
    #
    # except:
    #     raise ConnectionError
