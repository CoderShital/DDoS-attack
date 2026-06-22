from database.db import db, traffic_collection, blocked_collection, whitelisted_collection
from datetime import datetime
from pydantic import BaseModel


def init_db():
    """Initialize database collections"""
    try:
        # Create collections by inserting a dummy document and deleting it
        if "traffic_logs" not in db.list_collection_names():
            traffic_collection.insert_one({"_temp": True})
            traffic_collection.delete_one({"_temp": True})
            print("✓ Created 'traffic_logs' collection")
        
        if "blocked_ips" not in db.list_collection_names():
            blocked_collection.insert_one({"_temp": True})
            blocked_collection.delete_one({"_temp": True})
            print("✓ Created 'blocked_ips' collection")

        if "blocked_ips" not in db.list_collection_names():
            whitelisted_collection.insert_one({"_temp": True})
            whitelisted_collection.delete_one({"_temp": True})
            print("✓ Created 'whitelisted_ips' collection")
        
        # Add sample data for testing
        sample_traffic = [
            {
                "source_ip": "192.168.1.100",
                "endpoint": "/api/login",
                "request_count": 15,
                "status": "normal",
                "timestamp": datetime.now(),
                "blocked": False
            },
            {
                "source_ip": "10.0.0.50",
                "endpoint": "/api/data",
                "request_count": 85,
                "status": "normal",
                "timestamp": datetime.now(),
                "blocked": False
            }
        ]
        sample_blocked = [
            {
                "source_ip": "192.168.11.100",
                "endpoint": "/api/login",
                "request_count": 150,
                "status": "blocked",
                "timestamp": datetime.now(),
                "blocked": True
            },
            {
                "source_ip": "10.0.0.50",
                "endpoint": "/api/data",
                "request_count": 185,
                "status": "blocked",
                "timestamp": datetime.now(),
                "blocked": True
            }
        ]
        sample_whitelist = [
            {
                "source_ip": "192.168.1.112",
                "endpoint": "/api/login",
                "request_count": 15,
                "status": "whitelisted",
                "timestamp": datetime.now(),
                "blocked": False
            }
        ]
        
        if traffic_collection.count_documents({}) == 0 or blocked_collection.count_documents({}) == 0 or whitelisted_collection.count_documents({}) == 0:
            traffic_collection.insert_many(sample_traffic)
            blocked_collection.insert_many(sample_blocked)
            whitelisted_collection.insert_many(sample_whitelist)
            print("✓ Added sample data")
        
        print("\n✓ Database collections initialized successfully")
    except Exception as e:
        print(f"✗ Error initializing database: {e}")


if __name__ == "__main__":
    init_db()
