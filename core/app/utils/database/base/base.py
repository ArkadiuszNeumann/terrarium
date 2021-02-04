from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base as real_declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
import sqlalchemy

engine = create_engine('mysql://root:root@db/terra', echo=True)

if not database_exists(engine.url):
    create_database(engine.url)

_SessionFactory = sessionmaker(bind=engine)

declarative_base = lambda cls: real_declarative_base(cls=cls)


def session_factory(create_all=False):
    if create_all:
        Base.metadata.create_all(engine)
    return _SessionFactory()


@declarative_base
class Base(object):
    @property
    def columns(self):
        return [c.name for c in self.__table__.columns]

    @property
    def column_items(self):
        return dict([(c, getattr(self, c)) for c in self.columns])

    def __repr__(self):
        return "{}".format(self.column_items)

    def to_json(self):
        return self.column_items
