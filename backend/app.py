"""
Instantiation of Flask application
"""

from flask import Flask
import config

# Instantiate app
# Flask app must be created BEFORE you import modules that depend on it!
# Add them below instatiation of app.
app = Flask(__name__)

# Load configurations
app.config.from_object(config)


@app.route("/")
def hello_world():
    """
    Return 'Hello World'-paragraph.
    """
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    # Setting debug to True enables debug output if errors occur.
    #
    # ***IMPORTANT***: 'app.debug = True' should be commented out before deploying a production app!!!!
    # Good practice for development, but can reveal internal aspects of application
    # --> Security Threat.
    # app.debug = True
    app.run()
