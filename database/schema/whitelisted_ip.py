from pydantic import BaseModel
from datetime import datetime


class WhiteListed_IP(BaseModel):
    source_ip: str
    endpoint: str
    request_count: int
    status: str
    timestamp: datetime
    blocked:bool
    