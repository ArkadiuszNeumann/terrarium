from sqlalchemy import Column, Integer,Float, DateTime, ForeignKey
from ..base.base import Base
from datetime import datetime
from ..device import Device
from ..sensor import Sensor

class Humidity(Base):
    __tablename__ = 'humidity'
    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey(Device.id), nullable=False, index=True)
    sensor_id = Column(Integer, ForeignKey(Sensor.id), nullable=False, index=True)
    value = Column(Float)
    last_update = Column(Integer)
