from . import blog
from flask import render_template

@blog.route('/')
def home_page():
    return render_template("base.html")