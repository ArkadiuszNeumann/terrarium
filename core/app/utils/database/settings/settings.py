from sqlalchemy import Column, Integer, String, ForeignKey
from ..base.base import Base
from ..device import Device
from ..sensor import Sensor


class Settings(Base):
    __tablename__ = 'settings'
    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey(Device.id), nullable=False, index=True)
    sensor_id = Column(Integer, ForeignKey(Sensor.id), nullable=False, index=True)
    key = Column(String(15))
    value = Column(String(20))
    priority = Column(Integer)
