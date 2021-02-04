from app.utils.database.job import Job
from app.utils.database.base.base import session_factory
from app.utils.database.db_connection import *
from app.utils.database import pydantication
from .schema import Job


def add_job(req):
    try:
        response = pydantication.create_db_object(req, Settings, skip=["id"])
        insert_into_db(response)
    except:
        raise ConnectionError