import detector
import csv
from flask import Flask, request, render_template, jsonify
from ml_detector import train_model, predict_attack
from detector import request_log
from logger import log_request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/request")
def handle_request():
    global total_requests
    global blocked_requests

    total_requests += 1
    ip = request.remote_addr
    endpoint = request.path
    req_count = detect_attack(ip)

    # RULE-BASED CHECK
    if req_count > THRESHOLD:
        # ML CHECK
        ml_result = predict_attack(req_count)
        if ml_result == -1:
            blocked_requests += 1
            log_request(
                ip=ip,
                request_count=req_count,
                status="blocked",
                endpoint=endpoint
            )
            return render_template("ddos_blocked.html")
    # NORMAL TRAFFIC
    log_request(
        ip=ip,
        request_count=req_count,
        status="normal",
        endpoint=endpoint
    )
    return render_template("ippb_clone.html")

@app.route("/stats")
def stats():
    return jsonify({
        "total": detector.total_req,
        "blocked": detector.blocked_req
    })

@app.route("/logs")
def get_logs():
    logs = []
    with open("traffic_logs.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            logs.append(row)
    return jsonify(logs[-15:])

@app.route("/top-ip")
def top_ip():
    counts = {}
    try:
        with open("attacks.log", "r") as f:
            for line in f:
                ip = line.split("|")[-1].strip()
                counts[ip] = counts.get(ip, 0) + 1
        top = max(counts, key=counts.get) if counts else "None"
        return jsonify({"top_ip": top})
    except:
        return jsonify({"top_ip": "None"})

if __name__ == "__main__":
    app.run(debug=True)