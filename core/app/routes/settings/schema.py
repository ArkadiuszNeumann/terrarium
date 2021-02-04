from pydantic import BaseModel
from typing import Optional


class Settings(BaseModel):
    id: Optional[int] = None
    device_id: int = None
    sensor_id: Optional[int] = None
    key: str = None
    value: str = None
    priority: int = None
