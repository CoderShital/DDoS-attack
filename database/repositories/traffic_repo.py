from database.db import traffic_collection, blocked_collection

def save_traffic(traffic):
    # unknown = traffic_collection.find({"ip": "Unknown"})
    traffic_collection.insert_one(traffic)

def get_recent_logs(limit=15): 
    traffic_logs = list(
        traffic_collection
        .find({}, {"_id": 0})
        .sort("timestamp", -1)
        .limit(limit)
    )

    blocked_logs = list(
        blocked_collection
        .find({}, {"_id": 0})
        .sort("timestamp", -1)
        .limit(limit)
    )

    return traffic_logs + blocked_logs