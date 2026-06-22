from database.db import traffic_collection

def save_traffic(traffic):

    traffic_collection.insert_one(
        traffic
    )

def get_recent_logs(limit=15):

    return list(
        traffic_collection
        .find({}, {"_id": 0})
        .sort("timestamp", -1)
        .limit(limit)
    )