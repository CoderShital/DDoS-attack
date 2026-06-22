from flask import Blueprint, jsonify

from services.stats_service import (
    get_stats,
    get_recent_logs,
    get_top_ip
)

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)

@dashboard_bp.route("/stats")
def stats():
    try:
        return jsonify(get_stats())
    except Exception as e:
        print(f"Error in /stats: {e}")
        return jsonify({"total": 0, "blocked": 0, "status": "error"})

@dashboard_bp.route("/logs")
def logs():
    try:
        data = get_recent_logs()
       # print("--------------------------------------------------------------------------------------------------")
       # print(data)
        return jsonify(get_recent_logs())
    except Exception as e:
        print(f"Error in /logs: {e}")
        return jsonify([])

@dashboard_bp.route("/top-ip")
def top_ip():
    try:
        result = get_top_ip()
        if result is None:
            return jsonify({"top_ip": None})
        return jsonify(result)
    except Exception as e:
        print(f"Error in /top-ip: {e}")
        return jsonify({"top_ip": None})