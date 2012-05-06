import tornado.ioloop
import tornado.web
import db

import json

class KeyHandler(tornado.web.RequestHandler):
    def get(self, key):
        session = db.Session()
        self.set_header('Content-Type', 'application/json')
        try:
            values = session.query(db.Key).filter_by(key_name=key).all()[0].values
            self.write(map(lambda value:value.data, values))
        except:
            self.write('[]') #this is an ugly hack but w/e

    def post(self, key):
        data = self.request.body
        try:
            data = json.dumps(json.loads(data))
            session = db.Session()
            if session.query(db.Key).filter_by(key_name=key).count() == 0:
                new_key = db.Key(key_name=key)
            elif session.query(db.Key).filter_by(key_name=key).count() == 1:
                new_key = list(session.query(db.Key).filter_by(key_name=key))[0]
            session.add(new_key)
            session.commit()
            new_value = db.Value(data=data, key=new_key)
            session.add(new_value)
            session.commit()
            self.write('test')
            return
        except:
            self.write('invalid JSON')
            return

application = tornado.web.Application([
    (r"/([^/]*)/*$", KeyHandler),
], debug=True,)

if __name__ == "__main__":
    application.listen(800)
    tornado.ioloop.IOLoop.instance().start()