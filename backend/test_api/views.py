"""
Routes of TEST API
"""

from flask import Blueprint, jsonify


test_api_bp = Blueprint("test_api_bp", __name__)


# API for Test Purposes
@test_api_bp.route("/test-api/test1", methods=["GET"])
def users():
    """
    Test API: Return Users-JSON.
    """
    return jsonify({"users": ["Chris", "Sophia", "Augustinus"]})
