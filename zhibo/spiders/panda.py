from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import re
import string
from zhibo.items import ZhiboItem

class PandaSpider(BaseSpider):
   name = "panda"
   allowed_domains = ["panda.com"]
   start_urls = [
       "http://www.panda.tv/cate/dota2",
	"http://www.panda.tv/cate/lol",
	"http://www.panda.tv/cate/hearthstone",
	"http://www.panda.tv/cate/hwzb",
	"http://www.panda.tv/cate/yzdr"
   ]

   def parse(self, response):
        for sel in response.xpath('//div[@class = "list-container"]/ul/li'):
            		item = ZhiboItem()
			item['zhubo'] ="pandas"+sel.xpath('a/div[@class = "video-info"]/span[@class = "video-nickname"]/text()').extract()[0]
            		item['img_url'] = sel.xpath('a//img/@data-original').extract()[0]
			item['title'] = sel.xpath('a//img/@alt').extract()[0]
            		item['link'] = "http://www.panda.tv" + sel.xpath('a/@href').extract()[0]
			num = sel.xpath('a/div[@class="video-info"]/span[@class = "video-number"]/text()').extract()[0]
			if num.isdigit() == False:
				num = re.findall(r"\d+\.?\d*",num)
				a = string.atof(num[0]) * 10000
				num = '%d'%a
			item['view'] = num 
			item['web'] = "panda"
			item['active'] = "yes"
			
			web = response.url
			if web == self.start_urls[0]:
				item['cate'] = "dota2" 
			elif web == self.start_urls[1]:
				item['cate'] = "lol"
			elif web == self.start_urls[2]:
				item['cate'] = "ls"
			elif web == self.start_urls[4]:
				item['cate'] = "baby"
			else:
				item['cate'] = "other"	
	
            		yield item



