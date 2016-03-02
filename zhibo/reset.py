#coding=utf-8

from sqlalchemy import create_engine, Table, Column, Float, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from sqlalchemy import update
import os

Base = declarative_base()

class exeu(Base):
    __tablename__ = "exeu"

    tableID = Column(Integer, primary_key=True)
    used = Column(Integer)

class dota2(Base):
    __tablename__ = "dota2"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', String(200))
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    active =  Column('active', String(200))

class war3(Base):
    __tablename__ = "war3"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', String(200))
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    active =  Column('active', String(200)) 
 

class lol(Base):
    __tablename__ = "lol"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', String(200))
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    active =  Column('active', String(200)) 

class ls(Base):
    __tablename__ = "ls"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', String(200))
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    active =  Column('active', String(200))

class baby(Base):
    __tablename__ = "baby"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', String(200))
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    active =  Column('active', String(200)) 
 

class other(Base):
    __tablename__ = "other"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', String(200))
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    active =  Column('active', String(200)) 


class dota22(Base):
    __tablename__ = "dota22"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', String(200))
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    active =  Column('active', String(200)) 

class war32(Base):
    __tablename__ = "war32"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', String(200))
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    active =  Column('active', String(200)) 

class lol2(Base):
    __tablename__ = "lol2"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', String(200))
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    active =  Column('active', String(200)) 

class ls2(Base):
    __tablename__ = "ls2"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', String(200))
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    active =  Column('active', String(200))

class baby2(Base):
    __tablename__ = "baby2"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', String(200))
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    active =  Column('active', String(200)) 
 

class other2(Base):
    __tablename__ = "other2"

    id = Column(Integer, primary_key=True)
    title = Column('title', String(200))
    link = Column('link', String(200))
    view = Column('view', String(200))
    img_url = Column('img_url', String(200))
    zhubo = Column('zhubo', String(200))
    active =  Column('active', String(200)) 
	

#创建从Base派生的所有表
def createAll(eng):
	Base.metadata.create_all(eng)
	
#删除DB中所有的表	
def dropAll(eng):
	Base.metadata.drop_all(eng)

#删除数据库中从Base派生的所有表
	
#创建session对象
if __name__ == '__main__':
	#创建数据库引擎
	eng = create_engine('mysql://root:LOUbu123@localhost:3306/zhibo?charset=utf8',echo=False)
	
	#设置回显
	#eng.echo = True
	
	#创建DBSession类型
	DBSession = sessionmaker(bind=eng)
	
	#创建session对象
	session = DBSession()
		
try:
	#创建表
	#createAll(eng)

	i = session.query(func.count(exeu.used)).\
		filter(exeu.used==1).scalar()
	print i
	if i == 1:
	   	stmt = update(exeu).where(exeu.tableID==1).\
        		values(used = 0)
   		eng.execute(stmt)
	elif i == 0:
	   	stmt = update(exeu).where(exeu.tableID==1).\
        		values(used = 1)
   		eng.execute(stmt)
	for filename in os.listdir("."):
		if filename == "a1a.py":
			os.rename(filename, "back_pipelines.py")
		elif filename == "b2b.py":
			os.rename(filename, "pipelines.py")
	if i == 0:	
		session.query(dota2).filter(dota2.id > 0).\
    			update({"active":u"no"})
		session.query(lol).filter(lol.id > 0).\
    			update({"active":u"no"})
		session.query(ls).filter(ls.id > 0).\
    			update({"active":u"no"})
		session.query(other).filter(other.id > 0).\
    			update({"active":u"no"})
		session.query(baby).filter(baby.id > 0).\
    			update({"active":u"no"})
		session.query(war3).filter(war3.id > 0).\
    			update({"active":u"no"})
	elif i == 1:
		session.query(dota22).filter(dota22.id > 0).\
    			update({"active":u"no"})
		session.query(lol2).filter(lol2.id > 0).\
    			update({"active":u"no"})
		session.query(ls2).filter(ls2.id > 0).\
    			update({"active":u"no"})
		session.query(other2).filter(other2.id > 0).\
    			update({"active":u"no"})
		session.query(baby2).filter(baby2.id > 0).\
    			update({"active":u"no"})
		session.query(war32).filter(war32.id > 0).\
    			update({"active":u"no"})

		
	#创建新User对象
	#new_user = User(id='14', name='ad')
	
	#print(u'你好吗')
	
	#添加到session
	#session.add(new_user)
	
	#提交保存到数据库
	session.commit()
	
except BaseException,e:
	print('e.message=%s' % str(e.message))
	
finally:
	session.close()
	#eng.close()
	
	
	
	
	




