import tornado.ioloop
import tornado.web
from controllers.main_handler import MainHandler
from controllers.about_handler import AboutHandler
from routes import make_app


# def make_app():
#     return tornado.web.Application([
#         (r"/", MainHandler),
#         (r"/about", AboutHandler),
#         (r"/submit", )
#     ], template_path="./frontend/templates")

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()