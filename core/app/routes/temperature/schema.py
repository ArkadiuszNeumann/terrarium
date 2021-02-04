from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TemperatureResponse(BaseModel):
    sensor_id: int = None
    value: float = None
    last_update: int = None


class TemperatureRequest(BaseModel):
    device_id: int = None
    value: float = None
    start_from: Optional[datetime] = None
    end_with: Optional[datetime] = None
    last_update: Optional[int] = datetime.timestamp(datetime.now())
