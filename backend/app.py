"""
Instantiation of Flask application
"""

from flask import Flask, send_from_directory
import config


# Instantiate app
#
# Flask app must be created BEFORE you import modules that depend on it!
# Add them below instatiation of app.
#
# All HTML pages are in the frontend folder and
# **not** in a (Flask) templates folder.
# Therefore a static folder must be set.
app = Flask(__name__, static_folder="../frontend")


# Load configurations
app.config.from_object(config)


@app.route("/")
def home_page():
    """
    Render homepage
    """
    return send_from_directory(app.static_folder, "index.html")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path): # pylint: disable=W0613
    """
    Catch-all route to handle redirects for single-page application.

    Catch-all routes are used to match any URL that does not match
    any other route in the application.

    This is useful for displaying a 404 page or redirecting
    to a specific route when a user enters an invalid URL.
    """
    return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    # Setting debug to True enables debug output if errors occur.
    #
    # ***IMPORTANT***:
    # 'app.debug = True' should be commented out before deploying a production app!!!!
    # Good practice for development, but can reveal internal aspects of application
    # --> Security Threat.
    # app.debug = True
    app.run()
