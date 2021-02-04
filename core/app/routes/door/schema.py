from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class DoorResponse(BaseModel):
    sensor_id: int = None
    value: int = None
    last_update: int = None


class DoorRequest(BaseModel):
    device_id: int = None
    value: int = None
    start_from: Optional[datetime] = None
    end_with: Optional[datetime] = None
    last_update: Optional[int] = datetime.timestamp(datetime.now())
