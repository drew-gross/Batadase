import tornado.ioloop
import tornado.web
import db

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class KeyHandler(tornado.web.RequestHandler):
    def get(self, key):
        session = db.Session()
        obj = session.query(db.Key).filter_by(key_name=key).all()
        self.write(repr(obj[0].values))

    def post(self, key):
        data = self.request.body
        session = db.Session()
        if session.query(db.Key).filter_by(key_name=key).count() == 0:
            new_key = db.Key(key_name=key)
        elif session.query(db.Key).filter_by(key_name=key).count() == 1:
            new_key = list(session.query(db.Key).filter_by(key_name=key))[0]
        session.add(new_key)
        session.add(db.Value(data=data, key=new_key))
        session.commit()
        self.write('test1')

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/key/([^/]*)/*$", KeyHandler),
], debug=True,)

if __name__ == "__main__":
    application.listen(800)
    tornado.ioloop.IOLoop.instance().start()