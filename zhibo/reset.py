#coding=utf-8

from sqlalchemy import create_engine, Table, Column, Float, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from sqlalchemy import update
from models import exeu, db_connect, create_douyu_table, create_table

engine = db_connect()
create_douyu_table(engine)
DBsession = sessionmaker(bind=engine)
session = DBsession()	
lists = ['dota2','baby','ls','war3','other','lol']
try:
	suffix = ''
	i = session.query(func.count(exeu.used)).\
		filter(exeu.used==1).scalar()
	if i == 1:
		suffix = '2'
	   	stmt = update(exeu).where(exeu.tableID==1).\
        		values(used = 0)
   		engine.execute(stmt)
	elif i == 0:
	   	stmt = update(exeu).where(exeu.tableID==1).\
        		values(used = 1)
   		engine.execute(stmt)
	for game in lists:
		session.query(create_table(game+suffix)).filter(id > 0).\
    			update({"active":u"no"})

	session.commit()
	
except BaseException,e:
	print('e.message=%s' % str(e.message))
	
finally:
	session.close()
	#eng.close()
	
	
	
	
	




