import tornado.web


class SubmitHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("submit.html", title="Submit")

    def post(self):
        print(dir(self))
