import tornado.ioloop
import tornado.web


class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("about.html", title="About")