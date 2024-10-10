"""
Routes of Health Check
"""

from flask import Blueprint, jsonify
from common.status_codes import HTTP_200_OK


health_check_bp = Blueprint("health_check_bp", __name__)


@health_check_bp.route("/health-check")
def health_check():
    """
    Let them know our heart is still beating.
    """
    return jsonify(status=HTTP_200_OK, message="OK"), HTTP_200_OK
