from sqlalchemy import Column, Integer, String, DateTime
from ..base.base import Base
from datetime import datetime


class Device(Base):
    __tablename__ = 'device'
    id = Column(Integer, primary_key=True)
    friendly_name = Column(String(15), nullable=False, index=True)
    ip = Column(String(15))
    last_update = Column(Integer)
