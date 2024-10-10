"""
Instantiation of Flask application
"""

from flask import Flask
from flask_cors import CORS

from common import paths
import config
from home.views import home_bp
from test_api.views import test_api_bp


# Instantiate app
#
# Flask app must be created BEFORE you import modules that depend on it!
# Add them below instatiation of app.
#
# All HTML pages are in the frontend folder and
# **not** in a (Flask) templates folder.
# Therefore a static folder must be set.
app = Flask("Server E-Commerce Pokemon", static_folder=paths.CLIENT_FOLDER)

# Load configurations
app.config.from_object(config)

# Let the server accept CORS so that the frontend can access the backend, for example.
# For a start, everything is accepted. Can be adapted later.
cors = CORS(app, origins="*")


# Register Routes / Views using Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(test_api_bp)


if __name__ == "__main__":
    # Setting debug to True enables debug output if errors occur.
    #
    # ***IMPORTANT***:
    # 'app.debug = True' should be commented out before deploying a production app!!!!
    # Good practice for development, but can reveal internal aspects of application
    # --> Security Threat.
    # app.debug = True
    app.run()
