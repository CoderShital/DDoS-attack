from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BlockedIP(BaseModel):
    ip: str
    endpoint: str
    request_count: int
    reason: str
    blocked_by: str
    is_active: bool
    blocked_at: datetime
    unblocked_at: Optional[datetime] = None