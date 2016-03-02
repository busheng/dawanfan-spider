from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import re
import string
from zhibo.items import ZhiboItem

class DouyuSpider(BaseSpider):
   name = "douyu"
   allowed_domains = ["douyu.com"]
   start_urls = [
       "http://www.douyutv.com/directory/game/DOTA2",
	"http://www.douyutv.com/directory/game/LOL",
	"http://www.douyutv.com/directory/game/How",
	"http://www.douyutv.com/directory/game/TVgame",
	"http://www.douyutv.com/directory/game/mszb",
	"http://www.douyutv.com/directory/game/qmxx"
   ]

   def parse(self, response):
        for sel in response.xpath('//div[@id = "live-list-content"]/ul/li'):
            		item = ZhiboItem()
			item['zhubo'] = "douyus"+sel.xpath('a//span[@class = "dy-name ellipsis fl"]/text()').extract()[0]
            		item['img_url'] = sel.xpath('a//span[@class = "imgbox"]/img/@data-original').extract()[0]
			item['title'] = sel.xpath('a/@title').extract()[0]
            		item['link'] = "http://www.douyutv.com" + sel.xpath('a/@href').extract()[0]
			num =  sel.xpath('a//span[@class="dy-num fr"]/text()').extract()[0]
			if num.isdigit() == False:
				num = re.findall(r"\d+\.?\d*",num)
				a = string.atof(num[0]) * 10000
				num = '%d'%a
			item['view'] = num 		
			item['web'] = "douyu"
			item['active'] = "yes"
			web = response.url
			if web == self.start_urls[0]:
				item['cate'] = "dota2" 
			elif web == self.start_urls[1]:
				item['cate'] = "lol"
			elif web == self.start_urls[2]:
				item['cate'] = "ls"
			elif web == self.start_urls[4]:
				item['cate'] = "war3"
			elif web == self.start_urls[5]:
				item['cate'] = "baby"
			else:
				item['cate'] = "other"	
	
            		yield item

