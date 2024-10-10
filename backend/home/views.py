"""
Routes of Home Page
"""

from flask import Blueprint, send_from_directory
from common import paths


home_bp = Blueprint("home_bp", __name__)


@home_bp.route("/")
def home_page():
    """
    Render homepage
    """
    return send_from_directory(paths.CLIENT_FOLDER, paths.CLIENT_MAIN_HTML)


@home_bp.route("/", defaults={"path": ""})
@home_bp.route("/<path:path>")
def catch_all(path):  # pylint: disable=W0613
    """
    Catch-all route to handle redirects for single-page application.

    Catch-all routes are used to match any URL that does not match
    any other route in the application.

    This is useful for displaying a 404 page or redirecting
    to a specific route when a user enters an invalid URL.
    """
    return send_from_directory(paths.CLIENT_FOLDER, paths.CLIENT_MAIN_HTML)
