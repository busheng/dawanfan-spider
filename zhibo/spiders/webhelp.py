import re
import string
class Webhelp:
   #  1.dota2
   #  2.LOL
   #  3.lushi
   #  4.moshou war3
   #  5.baby
   #  6.other
   #  7.
   #
   #
   #
   #
   web_map = {
   'douyu' : [
       "http://www.douyutv.com/directory/game/DOTA2",
	"http://www.douyutv.com/directory/game/LOL",
	"http://www.douyutv.com/directory/game/How",
	"http://www.douyutv.com/directory/game/mszb",
	"http://www.douyutv.com/directory/game/qmxx",
	"http://www.douyutv.com/directory/game/TVgame"
   ],
   'huomao' : [
       "http://www.huomaotv.cn/channel/dota2", #1.doat2
       "http://www.huomaotv.cn/channel/lol",   #2.lol 
       "http://www.huomaotv.cn/channel/ls",    #3.lushi
       "",	                               #4.war3
       "",                                     #5.baby
       "http://www.huomaotv.cn/channel/sc2"    #6.other
   ],
   'huya' : [
        "http://www.huya.com/g/dota2",
	"http://lol.huya.com",
	"http://www.huya.com/g/393",
	"",
	"http://www.huya.com/g/1663",
	"http://www.huya.com/g/2" #dnf
   ],
   'panda' : [
       "http://www.panda.tv/cate/dota2",
	"http://www.panda.tv/cate/lol",
	"http://www.panda.tv/cate/hearthstone",
	"",
	"http://www.panda.tv/cate/yzdr",
	"http://www.panda.tv/cate/hwzb"

   ],
   'zhanqi' : [
       "http://www.zhanqi.tv/games/dota2",
	"http://www.zhanqi.tv/games/lol",
	"http://www.zhanqi.tv/games/how",
	"",
	"",
	"http://bb.zhanqi.tv/"
]}

   web_urls = []
   web_name = ''
   def __init__(self, web):
	self.web_name = web
	self.web_urls = self.web_map[self.web_name]	

  
   def getgame(self, link):
     
	res = ''
	if link == self.web_urls[0]:
		res = "dota2" 
	elif link == self.web_urls[1]:
		res = "lol"
	elif link == self.web_urls[2]:
		res = "ls"
	elif link == self.web_urls[3]:
		res = "war3"
	elif link == self.web_urls[4]:
		res = "baby"
	else:
		res = "other"	
	return res

   def getnum(self, num):
	num = num.replace(",","")	
	if num.isdigit() == False:
	   num = re.findall(r"\d+\.?\d*",num)
	   a = string.atof(num[0]) * 10000
	   num = '%d'%a
        return num			
