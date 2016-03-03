from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import re
import string
from webhelp import Webhelp
from zhibo.items import ZhiboItem

class HuomaoSpider(BaseSpider):
   name = "huomao"
   web_instance = Webhelp(name)
   start_urls = filter(None,web_instance.web_urls)

   def parse(self, response):
        for sel in response.xpath('//div[@id = "live-list"]/ul/li[a[div[not(@class = "off")]]]'):
            		item = ZhiboItem()
			item['zhubo'] = "huomao"+sel.xpath('a/p/span[@class="username"]/text()').extract()[0]
            		item['img_url'] = sel.xpath('a/img/@data-original').extract()[0]
			item['title'] = sel.xpath('a/h4/text()').extract()[0]
            		item['link'] = "http://www.huomaotv.cn" + sel.xpath('a/@href').extract()[0]
			num = sel.xpath('a/p/span[@class="view"]/text()').extract()[0]
			item['view'] = self.web_instance.getnum(num)
			item['web'] = "huomao"
			item['active'] = "yes"
			item['cate'] =self.web_instance.getgame(response.url)	
            		yield item



