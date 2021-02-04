from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from ..base.base import Base
from datetime import datetime


class Sensor(Base):
    __tablename__ = 'sensor'
    id = Column(Integer, primary_key=True)
    type = Column(String(15), nullable=False, index=True)
