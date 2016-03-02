from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import re
import string 
from zhibo.items import ZhiboItem

class ZhanqiSpider(BaseSpider):
   name = "zhanqi"
   allowed_domains = ["zhanqi.com"]
   start_urls = [
       "http://www.zhanqi.tv/games/dota2",
	"http://www.zhanqi.tv/games/lol",
	"http://www.zhanqi.tv/games/how",
	"http://bb.zhanqi.tv/"
   ]

   def parse(self, response):
        for sel in response.xpath('//div[@class = "live-list-tabc"]/ul/li'):
            		item = ZhiboItem()
			item['zhubo'] = "zhanqi"+sel.xpath('a/div[@class ="info-area"]/div[@class ="meat"]/span[@class = "anchor anchor-to-cut dv"]/text()').extract()[0]
            		item['img_url'] = sel.xpath('a/div[@class="imgBox"]/img/@src').extract()[0]
			item['title'] = sel.xpath('a/div[@class="imgBox"]/img/@alt').extract()[0]
            		item['link'] = "http://www.zhanqi.tv" + sel.xpath('a/@href').extract()[0]
			num = sel.xpath('a/div[@class ="info-area"]/div[@class ="meat"]/span/span[@class = "dv"]/text()').extract()[0]
			if num.isdigit() == False:
				num = re.findall(r"\d+\.?\d*",num)
				a = string.atof(num[0]) * 10000
				num = '%d'%a
			item['view'] = num 	
		 	item['web'] = "zhanqi"
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



