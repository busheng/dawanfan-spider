from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import re
import string
from zhibo.items import ZhiboItem

class HuomaoSpider(BaseSpider):
   name = "huomao"
   allowed_domains = ["huomao.cn"]
   start_urls = [
       "http://www.huomaotv.cn/channel/dota2",
       "http://www.huomaotv.cn/channel/lol",
       "http://www.huomaotv.cn/channel/ls",
       "http://www.huomaotv.cn/channel/sc2"
   ]

   def parse(self, response):
        for sel in response.xpath('//div[@id = "live-list"]/ul/li[a[div[not(@class = "off")]]]'):
            		item = ZhiboItem()
			item['zhubo'] = "huomao"+sel.xpath('a/p/span[@class="username"]/text()').extract()[0]
            		item['img_url'] = sel.xpath('a/img/@data-original').extract()[0]
			item['title'] = sel.xpath('a/h4/text()').extract()[0]
            		item['link'] = "http://www.huomaotv.cn" + sel.xpath('a/@href').extract()[0]
			num = sel.xpath('a/p/span[@class="view"]/text()').extract()[0]
			num = num.replace(",","")
			if num.isdigit() == False:
				num = re.findall(r"\d+\.?\d*",num)
				a = string.atof(num[0]) * 10000
				num = '%d'%a
			item['view'] = num 	
			item['web'] = "huomao"
			item['active'] = "yes"
			web = response.url
			if web == self.start_urls[0]:
				item['cate'] = "dota2" 
			elif web == self.start_urls[1]:
				item['cate'] = "lol"
			elif web == self.start_urls[2]:
				item['cate'] = "ls"
			else:
				item['cate'] = "other"	
	
            		yield item



