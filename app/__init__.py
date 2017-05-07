from flask import Flask
from .blog import blog

app = Flask(__name__)

#
app.register_blueprint(blog)