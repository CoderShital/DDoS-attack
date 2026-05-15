from collections import defaultdict
import time

request_log = defaultdict(list)
THRESHOLD = 20
TIME_WINDOW = 10

total_req = 0
blocked_req = 0

def detect_attack(ip, path):
    global total_req, blocked_req
    total_req += 1
    current_time = time.time()
    request_log[ip].append(current_time)

    request_log[ip] = [
        t for t in request_log[ip]
        if current_time - t < TIME_WINDOW
    ]

    if len(request_log[ip]) > THRESHOLD:
        blocked_req += 1
        return True
    if path != "/request":
        return False