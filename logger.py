
import csv
import os
from datetime import datetime
from database.repositories.traffic_repo import save_traffic
from database.schema.traffic_logs import TrafficLog

CSV_FILE = "traffic_logs.csv"


def log_request(ip, request_count, status, endpoint):
    """Log request to both CSV file and MongoDB"""
    
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as f:

        writer = csv.writer(f)

        if not file_exists:

            writer.writerow([
                "timestamp",
                "ip",
                "request_count",
                "status",
                "endpoint"
            ])

        writer.writerow([
            datetime.now(),
            ip,
            request_count,
            status,
            endpoint
        ])
    
    # Also save to MongoDB
    try:
        traffic_log = TrafficLog(
            source_ip=ip,
            endpoint=endpoint,
            request_count=request_count,
            status=status,
            timestamp=datetime.now()
        )
        save_traffic(traffic_log)
    except Exception as e:
        print(f"Error saving to MongoDB: {e}")