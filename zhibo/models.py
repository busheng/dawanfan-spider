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

def create_table(name):
    return type(name,(DeclarativeBase,), {
        "__tablename__":name,
	"id" : Column(Integer, primary_key=True),
   	"title" : Column('title', String(200)),
    	"link" : Column('link', String(200)),
    	"view" : Column('view', Integer),
    	"img_url" : Column('img_url', String(200)),
    	"zhubo" : Column('zhubo', String(200)),
    	"web" : Column('web', String(200)),
    	"cate" :  Column('cate', String(200)), 
    	"active" :  Column('active', String(200)),
    })

class exeu(DeclarativeBase):
    __tablename__ = "exeu"

    tableID = Column(Integer, primary_key=True)
    used = Column(Integer)


