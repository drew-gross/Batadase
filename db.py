from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db')
Base = declarative_base()

class Key(Base):
    __tablename__ = 'keys'

    id = Column(Integer, primary_key=True)
    key_name = Column(String)

    def __init__(self, key_name):
        self.key_name = key_name

class Value(Base):
    __tablename__ = 'values'

    id = Column(Integer, primary_key=True)
    data = Column(String)
    key_id = Column(Integer, ForeignKey('keys.id'))
    key = relationship('Key', backref=backref('values', order_by=id))

    def __init__(self, data, key):
        self.data = data
        self.key_id = key.id



Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)