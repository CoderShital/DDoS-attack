from flask import Blueprint, request, jsonify
from services.attack_service import analyze_request

extension_bp = Blueprint(
    "extension",
    __name__
)

@extension_bp.route(
    "/check",
    methods=["POST"]
)
def check():
    data = request.get_json()
    result = analyze_request(
        ip=request.remote_addr,
        endpoint=data.get("url"),
        request_count=1
    )
    return jsonify({
        "block": result["attack"],
        "attack_type": result.get(
            "attack_type"
        )
    })