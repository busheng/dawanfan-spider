from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import re
import string
from webhelp import Webhelp
from zhibo.items import ZhiboItem

class LongzhuSpider(BaseSpider):
   name = "longzhu"
   web_instance = Webhelp(name)
   start_urls = filter(None,web_instance.web_urls)

   def parse(self, response):
        for sel in response.xpath('//div[@id = "list-con"]/a'):
            		item = ZhiboItem()
			item['zhubo'] = "douyus"+sel.xpath('a//span[@class = "dy-name ellipsis fl"]/text()').extract()[0]
            		item['img_url'] = sel.xpath('a//span[@class = "imgbox"]/img/@data-original').extract()[0]
			item['title'] = sel.xpath('a/@title').extract()[0]
            		item['link'] = "http://www.douyutv.com" + sel.xpath('a/@href').extract()[0]
			num =  sel.xpath('a//span[@class="dy-num fr"]/text()').extract()[0]
			item['view'] = self.web_instance.getnum(num)
			item['web'] = "longzhu"
			item['active'] = "yes"
			item['cate'] =self.web_instance.getgame(response.url)
            		yield item



