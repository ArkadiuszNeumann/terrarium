from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Device(BaseModel):
    id: Optional[int] = None
    friendly_name: str = None
    ip: str = None
    last_update: Optional[int] = datetime.timestamp(datetime.now())



