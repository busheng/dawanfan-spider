# -*- coding: utf-8 -*-

# Define your item pipelines here
#busheng
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Table, Column, Float, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from sqlalchemy import update
from models import exeu, db_connect, create_douyu_table, create_table

class ZhiboPipeline(object):
    
    i = 0; 
    lists = ['dota2','baby','ls','war3','other','lol']
    table_list = {}
    def __init__(self):
        engine = db_connect()
        create_douyu_table(engine)
        self.Session = sessionmaker(bind=engine)
    	self.prepare()

    def prepare(self):
        session = self.Session()
	self.i = session.query(func.count(exeu.used)).\
		filter(exeu.used==1).scalar()
	suffix = ''
	if self.i == 0:
		suffix = '2'
	for game in self.lists:
		self.table_list[game] = create_table(game+suffix);

    def process_item(self, item, spider):
        session = self.Session()
	table_name = item['cate']
	tables = self.table_list
	ins = session.query(tables[table_name]).filter_by(zhubo=item['zhubo']).first()
	if ins: 
		_update_(ins,item)
	else:
        	zhibo = tables[table_name](**item)
        	session.add(zhibo)
        session.commit()
        return item


def _update_(ins, item):
	ins.title = item['title']
	ins.view = item['view']
	ins.img_url = item['img_url']
	ins.link = item['link']
	ins.active = item['active']
