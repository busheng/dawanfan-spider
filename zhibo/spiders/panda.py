from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import re
import string
from webhelp import Webhelp
from zhibo.items import ZhiboItem

class PandaSpider(BaseSpider):
   name = "panda"
   web_instance = Webhelp(name)
   start_urls = filter(None,web_instance.web_urls)

   def parse(self, response):
        for sel in response.xpath('//div[@class = "list-container"]/ul/li'):
            		item = ZhiboItem()
			item['zhubo'] ="pandas"+sel.xpath('a/div[@class = "video-info"]/span[@class = "video-nickname"]/text()').extract()[0]
            		item['img_url'] = sel.xpath('a//img/@data-original').extract()[0]
			item['title'] = sel.xpath('a//img/@alt').extract()[0]
            		item['link'] = "http://www.panda.tv" + sel.xpath('a/@href').extract()[0]
			num = sel.xpath('a/div[@class="video-info"]/span[@class = "video-number"]/text()').extract()[0]
			item['view'] = self.web_instance.getnum(num)
			item['web'] = "panda"
			item['active'] = "yes"
			item['cate'] =self.web_instance.getgame(response.url)  
          		yield item



