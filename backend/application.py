"""
Instantiation of Flask application
"""

from flask import Flask
from flask_cors import CORS

import config
from shared.utils.test_api.views import test_api_bp
from shared.utils.health_check.views import health_check_bp


# ==================== Instantiate App =============================
#
# ***************** Note about imports *****************
# Flask app must be created BEFORE you import modules that depend on it!
# Add them below instatiation of app.
# E. g. blueprints solve this problem and avoid circular imports.
#
# ********* Note about variable app / application *********
# The Flask app variable is normally called as 'app'.
# The app is hosted with AWS Elastic Beanstalk (EB).
# EB searches for 'application' instead of 'app' by default.
# This naming convention must be adhered to!
#
# ==================================================================
application = Flask("Server E-Commerce Pokemon Shop: Trainer's Trove")

# Load configurations
application.config.from_object(config)

# Let the server accept CORS so that the frontend can access the backend, for example.
# NOTE: Improve in future. For a start, everything is accepted. Can be adapted later.
cors = CORS(application, origins="*")

# Register Routes / Views using Blueprints (e. g. to avoid circular imports)
application.register_blueprint(test_api_bp)
application.register_blueprint(health_check_bp)


if __name__ == "__main__":
    # ==================== Server Debugging ====================
    # Setting debug to True enables debug output if errors occur.
    #
    # ***IMPORTANT***:
    # 'application.debug = True' should be commented out before deploying a production app!
    # Good practice for development, but can reveal internal aspects of application
    # --> Security Threat.
    # application.debug = True
    # ==========================================================

    # ==================== HTTPS Communication ====================
    # Server responses must run via HTTPS, as they could otherwise be blocked.
    #
    # For example, you can use a self-signed certificate
    # --> E.g. by adding the parameter "ssl_context='adhoc'" to the Flask run method call).
    #
    # Web browsers and other HTTP clients come pre-configured with a list of known and trusted CAs,
    # but obviously if you use a self-signed certificate
    # the CA is not going to be known and validation will fail.
    #
    # Implemented solution: Backend runs via AWS Elastic Beanstalk.
    # Additional AWS configuration undertaken to run communication over HTTPS.
    # ==========================================================

    application.run()
