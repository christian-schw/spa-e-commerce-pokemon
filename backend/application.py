"""
Instantiation of Flask application
"""

from flask import Flask
from flask_cors import CORS

import config  # pylint: disable=C0413
from test_api.views import test_api_bp  # pylint: disable=C0413
from health_check.views import health_check_bp  # pylint: disable=C0413


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
application.config.from_object(config)

# Let the server accept CORS so that the frontend can access the backend, for example.
# NOTE: Improve in future. For a start, everything is accepted. Can be adapted later.
cors = CORS(application, origins="*")

# Register Routes / Views using Blueprints
application.register_blueprint(test_api_bp)
application.register_blueprint(health_check_bp)


if __name__ == "__main__":
    # Setting debug to True enables debug output if errors occur.
    #
    # ***IMPORTANT***:
    # 'application.debug = True' should be commented out before deploying a production app!!!!
    # Good practice for development, but can reveal internal aspects of application
    # --> Security Threat.
    # application.debug = True
    application.run()
