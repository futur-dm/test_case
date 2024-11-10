import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html")

class SubmitHandler(tornado.web.RequestHandler):
    def post(self):
        firstname = self.get_argument("firstname")
        lastname = self.get_argument("lastname")
        middlename = self.get_argument("middlename")
        phone = self.get_argument("phone")
        message = self.get_argument("message")

        self.render("result.html", firstname=firstname, lastname=lastname, middlename=middlename, phone=phone, message=message)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/submit", SubmitHandler),
    ], template_path="frontend")

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)    
    tornado.ioloop.IOLoop.current().start()