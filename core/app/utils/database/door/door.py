from sqlalchemy import Column, Integer, DateTime, ForeignKey
from ..base.base import Base
from datetime import datetime
from ..device import Device
from ..sensor import Sensor


class Door(Base):
    __tablename__ = 'door'
    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey(Device.id), nullable=False, index=True)
    sensor_id = Column(Integer, ForeignKey(Sensor.id), nullable=False, index=True)
    value = Column(Integer)
    last_update = Column(Integer)
