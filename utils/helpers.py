from datetime import datetime, timezone
from collections import defaultdict
import time

def get_current_timestamp():
    return datetime.now(timezone.utc)

def calculate_request_rate(request_count, time_window):
    if time_window == 0:
        return 0
    return request_count / time_window

def serialize_document(doc):
    doc["_id"] = str(doc["_id"])
    return doc
# Stores request history per IP
request_tracker = defaultdict(list)

def extract_features(ip, endpoint):
    current_time = time.time()

    # Track requests from same IP
    request_tracker[ip].append(current_time)

    # Keep only last 60 seconds requests
    request_tracker[ip] = [
        t for t in request_tracker[ip]
        if current_time - t <= 60
    ]

    request_count = len(request_tracker[ip])

    # Request rate
    request_rate = request_count / 60

    # Initialize all 77 features
    features = [0.0] * 77

    # -------------------------
    # Realistic Features
    # -------------------------

    # Protocol (TCP assumed)
    features[0] = 6

    # Flow Duration
    features[1] = 60

    # Total Fwd Packets
    features[2] = request_count

    # Total Backward Packets
    features[3] = 1

    # Flow Bytes/s
    features[14] = len(endpoint) * request_rate

    # Flow Packets/s
    features[15] = request_rate

    # Fwd Header Length
    features[34] = len(endpoint)

    # Fwd Packets/s
    features[36] = request_rate

    # Packet Length Min
    features[38] = len(endpoint)

    # Packet Length Max
    features[39] = len(endpoint)

    # Packet Length Mean
    features[40] = len(endpoint)

    # SYN Flag Count
    features[44] = 1

    # ACK Flag Count
    features[47] = 1

    # Avg Packet Size
    features[52] = len(endpoint)

    # Subflow Fwd Packets
    features[61] = request_count

    # Subflow Fwd Bytes
    features[62] = len(endpoint)

    # Init Fwd Win Bytes
    features[65] = 1024

    # Fwd Act Data Packets
    features[67] = request_count

    # Active Mean
    features[69] = request_rate

    # Idle Mean
    features[73] = max(0, 60 - request_count)

    return features