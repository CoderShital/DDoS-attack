
import csv
import os
from datetime import datetime

CSV_FILE = "traffic_logs.csv"


def log_request(ip, request_count, status, endpoint):

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