from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from ..base.base import Base
from datetime import datetime
from ..settings import Settings
from ..sensor import Sensor


class Jobs(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    settings_id = Column(Integer, ForeignKey(Settings.id), nullable=False, index=True)
    sensor_id = Column(Integer, ForeignKey(Sensor.id), nullable=False, index=True)
    state = Column(String(10))
    # TODO: Add format parser
    interval = Column(String(10))           # Format: D0-H0-M0-S0    >> Days, Hours, Minutes, Seconds
    last_run = Column(DateTime())
    next_run = Column(DateTime())
  