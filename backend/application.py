"""
Instantiation of Flask application
"""

# ========== Standard Imports ==========
# TODO: Delete this comment if not needed after deploying Flask!  # pylint: disable=W0511
# from sys import path


# ========== Third Party Imports ==========
from flask import Flask, render_template
from flask_cors import CORS

# TODO: Delete this comment if not needed after deploying Flask!  # pylint: disable=W0511
from werkzeug.middleware.proxy_fix import ProxyFix


# ========== Internal Imports ==========
# TODO: Delete this comment if not needed after deploying Flask!  # pylint: disable=W0511
# Make internal imports / module **explicitly** discoverable
# Reason: AWS Elastic Beanstalk can't find them if they are
#  **implicitly** discoverable. AWS EB pushes me to my limit...
#  I took the AWS path from the error message in AWS EB logs.
#
# NOTE: The modules imported in this py-file
# must be kept up to date here for the deployment to work!
# AWS_PATH = "/var/app/current/"
# BACKEND_FOLDER = "backend/"
# backend_modules = ["common", "health_check", "home", "test_api"]
# backend_paths = [AWS_PATH + BACKEND_FOLDER + module for module in backend_modules]
# path.append(backend_paths)


# from common import paths  # pylint: disable=C0413
# import config  # pylint: disable=C0413
# from home.views import home_bp  # pylint: disable=C0413
# from test_api.views import test_api_bp  # pylint: disable=C0413
# from health_check.views import health_check_bp  # pylint: disable=C0413


# ==================== Instantiate App =============================
#
# Flask app must be created BEFORE you import modules that depend on it!
# Add them below instatiation of app.
#
# ********* Note about variable app / application *********
# The Flask app variable is normally called as 'app'.
# The website is hosted with AWS Elastic Beanstalk (EB).
# EB searches for 'application' instead of 'app' by default.
# This naming convention must be adhered to!
application = Flask("Server E-Commerce Pokemon Shop: Trainer's Trove")

# Load configurations
# application.config.from_object(config)

# Let the server accept CORS so that the frontend can access the backend, for example.
# NOTE: For a start, everything is accepted. Can be adapted later.
cors = CORS(application, origins="*")

# TODO: Delete this comment if not needed after deploying Flask application!  # pylint: disable=W0511
# Tell Flask it's behind a proxy.
# For more information, see Flask documentation:
# 'Deploy to Production' -> 'Tell Flask it is Behind a Proxy'.
# application.wsgi_app = ProxyFix(
#     application.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
# )

# Register Routes / Views using Blueprints
# application.register_blueprint(home_bp)
# application.register_blueprint(test_api_bp)
# application.register_blueprint(health_check_bp)


@application.route("/")
def home_page():
    """
    Test Rendering for Deploying AWS EB
    """
    return "<h1>Hi! Flask Application running! :-)"


if __name__ == "__main__":
    # Setting debug to True enables debug output if errors occur.
    #
    # ***IMPORTANT***:
    # 'application.debug = True' should be commented out before deploying a production app!!!!
    # Good practice for development, but can reveal internal aspects of application
    # --> Security Threat.
    # application.debug = True
    application.run()
