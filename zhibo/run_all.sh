#!/bin/bash
#!/bin/bash
export PATH=$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
cd /root/spider/zhibo
python /root/spider/zhibo/reset.py
scrapy crawl panda
scrapy crawl huya
scrapy crawl douyu
scrapy crawl huomao
scrapy crawl zhanqi



