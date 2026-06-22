from pydantic import BaseModel
from datetime import datetime


class TrafficLog(BaseModel):
    source_ip: str
    endpoint: str
    request_count: int
    status: str
    timestamp: datetime