from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declared_attr

import settings


DeclarativeBase = declarative_base()


def db_connect():
   # return create_engine(URL(**settings.DATABASE))
   return create_engine('mysql://root:LOUbu123@localhost:3306/zhibo?charset=utf8',echo=False)

def create_douyu_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Zhibo_dota2(DeclarativeBase):
    __tablename__ = "dota2"
	
    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', Integer)
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    web = Column('web', String(200))
    cate =  Column('cate', String(200)) 
    active =  Column('active', String(200))

class Zhibo_war3(DeclarativeBase):
    __tablename__ = "war3"
	
    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', Integer)
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    web = Column('web', String(200))
    cate =  Column('cate', String(200)) 
    active =  Column('active', String(200)) 
 

class Zhibo_lol(DeclarativeBase):
    __tablename__ = "lol"
	
    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', Integer)
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    web = Column('web', String(200))
    cate =  Column('cate', String(200))
    active =  Column('active', String(200)) 

class Zhibo_ls(DeclarativeBase):
    __tablename__ = "ls"
	
    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', Integer)
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    web = Column('web', String(200))
    cate =  Column('cate', String(200))
    active =  Column('active', String(200)) 

class Zhibo_other(DeclarativeBase):
    __tablename__ = "other"
	
    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', Integer)
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    web = Column('web', String(200))
    cate =  Column('cate', String(200))
    active =  Column('active', String(200))

class Zhibo_baby(DeclarativeBase):
    __tablename__ = "baby"
	
    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', Integer)
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    web = Column('web', String(200))
    cate =  Column('cate', String(200))
    active =  Column('active', String(200)) 
 

class Zhibo_dota22(DeclarativeBase):
    __tablename__ = "dota22"
	
    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', Integer)
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    web = Column('web', String(200))
    cate =  Column('cate', String(200)) 
    active =  Column('active', String(200))
 
class Zhibo_war32(DeclarativeBase):
    __tablename__ = "war32"
	
    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', Integer)
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    web = Column('web', String(200))
    cate =  Column('cate', String(200)) 
    active =  Column('active', String(200)) 

class Zhibo_lol2(DeclarativeBase):
    __tablename__ = "lol2"
	
    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', Integer)
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    web = Column('web', String(200))
    cate =  Column('cate', String(200))
    active =  Column('active', String(200)) 

class Zhibo_ls2(DeclarativeBase):
    __tablename__ = "ls2"
	
    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', Integer)
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    web = Column('web', String(200))
    cate =  Column('cate', String(200))
    active =  Column('active', String(200)) 

class Zhibo_other2(DeclarativeBase):
    __tablename__ = "other2"
	
    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', Integer)
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    web = Column('web', String(200))
    cate =  Column('cate', String(200))
    active =  Column('active', String(200))

class Zhibo_baby2(DeclarativeBase):
    __tablename__ = "baby2"
	
    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', Integer)
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    web = Column('web', String(200))
    cate =  Column('cate', String(200))
    active =  Column('active', String(200)) 
 

