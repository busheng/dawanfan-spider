# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import Zhibo_dota22, Zhibo_lol2, Zhibo_ls2, Zhibo_other2, Zhibo_baby2, db_connect, create_douyu_table

class ZhiboPipeline(object):

    def __init__(self):
        engine = db_connect()
        create_douyu_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
	if item['cate'] == "dota2":
		ins = session.query(Zhibo_dota22).filter_by(zhubo=item['zhubo']).first()
		if ins: 
			_update_(ins,item)
		else:
        		zhibo = Zhibo_dota22(**item)
        		session.add(zhibo)
	elif item['cate'] == "lol":
		ins = session.query(Zhibo_lol2).filter_by(zhubo=item['zhubo']).first()
		if ins: 
			_update_(ins,item)
		else:
        		zhibo = Zhibo_lol2(**item)
        		session.add(zhibo)
	elif item['cate'] == "ls":
		ins = session.query(Zhibo_ls2).filter_by(zhubo=item['zhubo']).first()
		if ins: 
			_update_(ins,item)
		else:
        		zhibo = Zhibo_ls2(**item)
        		session.add(zhibo)
	elif item['cate'] == "baby":
		ins = session.query(Zhibo_baby2).filter_by(zhubo=item['zhubo']).first()
		if ins: 
			_update_(ins,item)
		else:
        		zhibo = Zhibo_baby2(**item)
        		session.add(zhibo)
	else:         	
		ins = session.query(Zhibo_other2).filter_by(zhubo=item['zhubo']).first()
		if ins: 
			_update_(ins,item)
		else:
        		zhibo = Zhibo_other2(**item)
        		session.add(zhibo)
        session.commit()
        return item

def _update_(ins, item):
	ins.title = item['title']
	ins.view = item['view']
	ins.img_url = item['img_url']
	ins.link = item['link']
	ins.active = item['active']
