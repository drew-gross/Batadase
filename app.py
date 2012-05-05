import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class KeyHandler(tornado.web.RequestHandler):
    def get(self, key):
        self.write(key)

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/key/(.*)", KeyHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()