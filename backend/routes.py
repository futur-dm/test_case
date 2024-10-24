import tornado.web
from controllers.main_handler import MainHandler
from controllers.about_handler import AboutHandler
from controllers.submit import SubmitHandler


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/about", AboutHandler),
        (r"/submit", SubmitHandler)
    ], template_path="./frontend/templates")