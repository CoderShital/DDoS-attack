from collections import defaultdict
import time

request_log = defaultdict(list)

THRESHOLD = 20
TIME_WINDOW = 10

total_req = 0
blocked_req = 0


def detect_attack(ip):
    global total_req
    total_req += 1
    current_time = time.time()

    # store current request time
    request_log[ip].append(current_time)

    # keep only recent requests
    request_log[ip] = [
        t for t in request_log[ip]
        if current_time - t < TIME_WINDOW
    ]

    # return current request count
    return len(request_log[ip])