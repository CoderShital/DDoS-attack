from database.repositories.traffic_repo import get_recent_logs as repo_get_recent_logs
from database.repositories.blocked_ip_repo import get_all_blocked_ips

def get_stats():
    """Get overall statistics about attacks and mitigation"""
    traffic_logs = repo_get_recent_logs(limit=1000)
    # Count total requests from traffic logs
    total = len(traffic_logs)
    # Count blocked requests (traffic logs with blocked status or status="blocked")
    blocked = sum(1 for log in traffic_logs if log.get("status") == "blocked" or log.get("blocked"))
    
    return {
        "total": total,
        "blocked": blocked,
        "status": "active"
    }


def get_recent_logs(limit=15):
    """Get recent traffic logs formatted for display"""
    logs = repo_get_recent_logs(limit)
    
    # Format logs for frontend 
    formatted_logs = []
    for log in logs:
        formatted_logs.append({
            "ip": log.get("source_ip", "Unknown"),
            "timestamp": str(log.get("timestamp", "")),
            "status": ("blocked" 
                       if log.get("blocked") or log.get("source_ip", "Unknown") == "Unknown" 
                       else "normal"),
            "request_count": log.get("request_count", 0)
        }) 
    return formatted_logs


def get_top_ip():
    """Get the top attacking IP address"""
    traffic_logs = repo_get_recent_logs(limit=1000)

    
    if not traffic_logs:
        return {"top_ip": None}
    
    # Count requests by source IP
    ip_counts = {}
    for log in traffic_logs:
        ip = log.get("source_ip", "Unknown")
        ip_counts[ip] = ip_counts.get(ip, 0) + log.get("request_count", 1)
    
    # Return the IP with most requests
    if ip_counts:
        top_ip = max(ip_counts.items(), key=lambda x: x[1])[0]
        return {"top_ip": top_ip}
    
    return {"top_ip": None}