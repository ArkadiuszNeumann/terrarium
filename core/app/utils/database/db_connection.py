import mysql.connector
from sqlalchemy.orm.query import Query
from .base.base import session_factory
from datetime import datetime
from app.utils.database import pydantication
import logging

logger = logging.getLogger(__name__)

def select_one(query):
    try:
        return query.one_or_none()
    except:
        return None


def select_all(query):
    try:
        return query.all()
    except:
        return None


def select_query_from_db(obj, close_session=True, session=None):
    if session is None:
        session = session_factory()
    result = session.query(obj)
    if close_session:
        session.close()
    return result


def select_all_from_db(obj, close_session=True, session=None):
    if session is None:
        session = session_factory()
    result = session.query(obj)
    if close_session:
        try:
            result = select_all(result)
        except:
            result = None
        session.close()
    return result


def select_newest_from_db(obj, close_session=True, session=None):
    if session is None:
        session = session_factory()
    result = session.query(obj).order_by(obj.id.desc()).first()
    if close_session:
        try:
            result = select_all(result)
        except:
            result = None
        session.close()
    return result


def update_row(obj, attributes_dict, close_session=True, session=None):
    if session is None:
        session = session_factory()
    for key in attributes_dict:
        if key.startswith("_"):
            continue
        setattr(obj, key, attributes_dict[key])
    session.commit()
    if close_session:
        session.close()


def insert_into_db(obj, close_session=True, session=None):
    if session is None:
        session = session_factory()
    session.add(obj)
    session.commit()
    id = obj.id
    if close_session:
        session.close()
    return id


def delete_from_db(obj, close_session=True, session=None):
    if session is None:
        session = session_factory()
    session.delete(obj)
    session.commit()
    if close_session:
        session.close()
