from flask import Flask
from flask_bootstrap import Bootstrap
from .blog import blog

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)

    app.register_blueprint(blog)
    return app