from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import re
import string
from webhelp import Webhelp
from zhibo.items import ZhiboItem

class HuyaSpider(BaseSpider):
   name = "huya"
   web_instance = Webhelp(name)
   start_urls = filter(None,web_instance.web_urls)

   def parse(self, response):
        for sel in response.xpath('//div[@class = "video-unit"]/ul/li'):
            		item = ZhiboItem()
			item['zhubo'] = "huyass"+sel.xpath('a//img/@title').extract()[0]
            		item['img_url'] = sel.xpath('a//img/@src').extract()[0]
			item['title'] = sel.xpath('div/a/text()').extract()[0]
            		item['link'] = sel.xpath('a/@href').extract()[0]
			num = sel.xpath('span[@class ="txt all_live_txt"]/span[@class="num"]/i/text()').extract()[0]
			item['view'] = self.web_instance.getnum(num)
			item['web'] = "huya"
			item['active'] = "yes"
			item['cate'] =self.web_instance.getgame(response.url)    
        		yield item



