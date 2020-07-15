from flask import Flask
from .extensions import mongo
from .main import main
from settings import Config


def create_app():
    app = Flask(__name__,instance_relative_config=False)

    app.config.from_object(Config)

    mongo.init_app(app)

    with app.app_context():
        app.register_blueprint(main)

        return app

