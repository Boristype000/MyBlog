from . import blog

@blog.route('/')
def home_page():
    return "Hello World!---from Blueprint!"