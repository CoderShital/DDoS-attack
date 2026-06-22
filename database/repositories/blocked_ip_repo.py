from database.schema.blocked_ip import BlockedIP
from database.db import blocked_collection

def save_blocked_ip(blocked_ip:BlockedIP):
    existing = blocked_collection.find_one(
        {
            "ip" : blocked_ip.ip,
            "is_active" : True
        }
    )
    if not existing:
        blocked_collection.insert_one(
            blocked_ip.model_dump()
        )

def get_all_blocked_ips():
    return list(
        blocked_collection.find(
            {},
            {"_id":0}
        )
        )