from . import blog
from flask import render_template

@blog.route('/')
def home_page():
    return render_template("index.html")

@blog.route('/about')
def about_me():
    return render_template("about.html")

@blog.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@blog.app_errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"),500