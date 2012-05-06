import tornado.ioloop
import tornado.web
import db

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class KeyHandler(tornado.web.RequestHandler):
    def get(self, key):
        session = db.Session()
        values = session.query(db.Key).filter_by(key_name=key).all()[0].values
        self.set_header('Content-Type', 'application/json')
        self.write(str(map(lambda value:value.data, values)))

    def post(self, key):
        data = self.request.body
        session = db.Session()
        if session.query(db.Key).filter_by(key_name=key).count() == 0:
            new_key = db.Key(key_name=key)
        elif session.query(db.Key).filter_by(key_name=key).count() == 1:
            new_key = list(session.query(db.Key).filter_by(key_name=key))[0]
        session.add(new_key)
        new_value = db.Value(data=data, key=new_key)
        session.add(new_value)
        session.commit()
        self.write('test1')

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/key/([^/]*)/*$", KeyHandler),
], debug=True,)

if __name__ == "__main__":
    application.listen(800)
    tornado.ioloop.IOLoop.instance().start()