from flask import Blueprint, render_template, request
from services.attack_service import process_request
from database.db import traffic_collection

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("index.html")

@main_bp.route("/requests")
def service_page():
    return render_template("ippb_clone.html")

@main_bp.route("/request", methods=["GET", "POST"])
def handle_request():
    ip = request.remote_addr
    endpoint = request.path
    request_count = traffic_collection.count_documents(
        {"source_ip": ip}
    ) + 1
    result = process_request(
        ip=ip,
        endpoint=endpoint,
        request_count=request_count
    )
    return result