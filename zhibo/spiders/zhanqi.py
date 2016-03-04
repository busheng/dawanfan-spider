from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import re
import string
from webhelp import Webhelp 
from zhibo.items import ZhiboItem

class ZhanqiSpider(BaseSpider):
   name = "zhanqi"
   web_instance = Webhelp(name)
   start_urls = filter(None,web_instance.web_urls)

   def parse(self, response):
        for sel in response.xpath('//div[@class = "live-list-tabc" and not(p[@class = "no-videoList-title"])]/ul/li | //div[@class = "bb-hot-area bb-funny-area bb-room-list" or @class ="bb-variety-area bb-room-list"]/div[@class = "bd"]/ul/li'):
            		item = ZhiboItem()
			item['zhubo'] = "zhanqi"+sel.xpath('a/div[@class ="info-area"]/div[@class ="meat"]/span[@class = "anchor anchor-to-cut dv"]/text()').extract()[0]
            		item['img_url'] = sel.xpath('a/div[@class="imgBox"]/img/@src').extract()[0]
			item['title'] = sel.xpath('a/div[@class="imgBox"]/img/@alt').extract()[0]
            		item['link'] = "http://www.zhanqi.tv" + sel.xpath('a/@href').extract()[0]
			num = sel.xpath('a/div[@class ="info-area"]/div[@class ="meat"]/span/span[@class = "dv"]/text()').extract()[0]
			item['view'] = self.web_instance.getnum(num)
		 	item['web'] = "zhanqi"
			item['active'] = "yes"
			item['cate'] =self.web_instance.getgame(response.url)	
            		yield item



