from flask import Flask
from .extensions import mongo
from .main import main
from settings import Config


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    mongo.init_app(app)

    app.register_blueprint(main)

    return app

