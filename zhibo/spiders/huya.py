from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import re
import string
from zhibo.items import ZhiboItem

class HuyaSpider(BaseSpider):
   name = "huya"
   allowed_domains = ["huya.com"]
   start_urls = [
       "http://www.huya.com/g/dota2",
	"http://lol.huya.com",
	"http://www.huya.com/g/393",
	"http://www.huya.com/g/2",
	"http://www.huya.com/g/1663"
   ]

   def parse(self, response):
        for sel in response.xpath('//div[@class = "video-unit"]/ul/li'):
            		item = ZhiboItem()
			item['zhubo'] = "huyass"+sel.xpath('a//img/@title').extract()[0]
            		item['img_url'] = sel.xpath('a//img/@src').extract()[0]
			item['title'] = sel.xpath('div/a/text()').extract()[0]
            		item['link'] = sel.xpath('a/@href').extract()[0]
			num = sel.xpath('span[@class ="txt all_live_txt"]/span[@class="num"]/i/text()').extract()[0]
			if num.isdigit() == False:
				num = re.findall(r"\d+\.?\d*",num)
				a = string.atof(num[0]) * 10000
				num = '%d'%a
			item['view'] = num 	
			item['web'] = "huya"
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



