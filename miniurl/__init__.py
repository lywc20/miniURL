from flask import Flask, render_template
from .extensions import mongo
from .main import main
from instance.settings import Config

def page_not_found(e):
    return render_template('404.html'),404

def create_app(test_config = None):
    app = Flask(__name__,instance_relative_config=True)

    if test_config is None:
        app.config.from_object(Config)
        mongo.init_app(app)
    else:
        app.config.update(test_config)


    with app.app_context():
        app.register_blueprint(main)
        app.register_error_handler(404,page_not_found)
        return app
