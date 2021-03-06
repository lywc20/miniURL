from flask import Flask, render_template
from .extensions import mongo
from .main import main
from instance.settings import Config

def page_not_found(e):
    return render_template('404.html'),404

def create_app():
    app = Flask(__name__,instance_relative_config=True)

    app.config.from_object(Config)
    mongo.init_app(app)



    with app.app_context():
        app.register_blueprint(main)
        app.register_error_handler(404,page_not_found)
        return app
