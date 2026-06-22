from flask import render_template
from detection.detector_service import detect_attack
from utils.helpers import (
    extract_features,
    get_current_timestamp
)
from database.db import blocked_collection
from database.repositories.traffic_repo import (
    save_traffic
)
from database.schema.blocked_ip import BlockedIP
from database.repositories.blocked_ip_repo import save_blocked_ip
from utils.helpers import get_current_timestamp
from config import WHITELISTED_IPS

def analyze_request(ip, endpoint, request_count):
    # For whitelisted IPs
    if ip in WHITELISTED_IPS:
        whitelisted_ips = {
            "source_ip": ip,
            "endpoint": endpoint,
            "timestamp": get_current_timestamp(),
            "blocked": False,
            "status": "whitelisted",
            "request_count": request_count,
            "attack_type": "Whitelisted IP"
        }
        save_traffic(whitelisted_ips)
        return {
            "attack": False,
            "attack_type": "Whitelisted IP"
        }
    # Already blocked IP
    existing = blocked_collection.find_one(
        {
            "ip": ip,
            "is_active": True
        }
    )
    if existing:
        return {
            "attack": True,
            "attack_type": "IP Already Blocked"
        }
    features = extract_features(ip, endpoint)
    result = detect_attack(features)
    traffic_log = {
        "source_ip": ip,
        "endpoint": endpoint,
        "timestamp": get_current_timestamp(),
        "blocked": result["attack"],
        "status": (
            "blocked"
            if result["attack"]
            else "normal"
        ),
        "request_count": request_count,
        "attack_type": result.get(
            "attack_type",
            "Benign"
        )
    }
    save_traffic(traffic_log)
    if result["attack"]:
        blocked_ip = BlockedIP(
            ip=ip,
            endpoint=endpoint,
            request_count=request_count,
            reason=result.get(
                "attack_type",
                "DDoS Attack"
            ),
            blocked_by=result.get(
                "source",
                "ml_model"
            ),
            is_active=True,
            blocked_at=get_current_timestamp()
        )
        save_blocked_ip(blocked_ip)
    return result


def process_request(ip, endpoint, request_count):
    result = analyze_request(
        ip,
        endpoint,
        request_count
    )
    if result["attack"]:
        return render_template(
            "ddos_blocked.html",
            attack_type=result.get(
                "attack_type"
            )
        )
    return render_template(
        "ippb_clone.html"
    )