from flask import Flask
from .model import mail_processor, app_exceptions

def create_app():
    app = Flask(__name__)
    from .routes import register_routes
    register_routes(app)

    return app
