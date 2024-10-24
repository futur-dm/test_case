import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", title="Home Page", items=["Item 1", "Item 2", "Item 3"])
