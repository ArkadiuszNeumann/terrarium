from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Relay(BaseModel):
    device_id: int = None
    sensor_id: int = None
    status: Optional[int] = None
    last_update: Optional[int] = datetime.timestamp(datetime.now())
