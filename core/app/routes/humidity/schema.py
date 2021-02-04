from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class HumidityResponse(BaseModel):
    sensor_id: int = None
    value: float = None
    last_update: int = None


class HumidityRequest(BaseModel):
    device_id: int = None
    value: float = None
    start_from: Optional[datetime] = None
    end_with: Optional[datetime] = None
    last_update: Optional[int] = datetime.timestamp(datetime.now())
