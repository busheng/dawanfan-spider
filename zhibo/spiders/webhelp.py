import re
import string
class Webhelp:
   #  0.dota2
   #  1.LOL
   #  2.lushi
   #  3.moshou war3
   #  4.baby
   #  5.WOW
   #  6.DNF
   #  7.CF
   #  8.other
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
	"http://www.douyutv.com/directory/game/WOW",
	"http://www.douyutv.com/directory/game/DNF",
	"http://www.douyutv.com/directory/game/CF",
	"http://www.douyutv.com/directory/game/TVgame"
   ],
   'huomao' : [
       "http://www.huomaotv.cn/channel/dota2", #0.doat2
       "http://www.huomaotv.cn/channel/lol",   #1.lol 
       "http://www.huomaotv.cn/channel/ls",    #2.lushi
       "",	                               #3.war3
       "",                                     #4.baby
       "",    				       #5.WOW
       "",    				       #6.DNF
       "",    				       #7.CF
       "",    				       #8.
       "http://www.huomaotv.cn/channel/sc2"    #9.other
   ],
   'huya' : [
        "http://www.huya.com/g/dota2",         #0.dota2
	"http://lol.huya.com",                 #1.lol
	"http://www.huya.com/g/393",   	       #2.lushi
	"",                                    #3.war3
	"http://www.huya.com/g/1663",          #4.baby
        "",    				       #5.WOW
        "http://www.huya.com/g/2", 	       #6.DNF
        "",    				       #7.CF
        "",    				       #8.
    ],
   'panda' : [
       "http://www.panda.tv/cate/dota2",	#0.dota2
	"http://www.panda.tv/cate/lol",         #1.lol
	"http://www.panda.tv/cate/hearthstone", #2.lushi
	"",                                     #3.war3
	"http://www.panda.tv/cate/yzdr", 	#4.baby
        "",    				        #5.WOW
        "",    				        #6.DNF
        "",    				        #7.CF
	"http://www.panda.tv/cate/hwzb"  	#8other

   ],
   'longzhu' : [
        "",
	"http://longzhu.com/channels/lol",
	"",
	"",
	"",
	""

   ],
   'zhanqi' : [
       "http://www.zhanqi.tv/games/dota2",	#0.dota2
	"http://www.zhanqi.tv/games/lol", 	#1.lol
	"http://www.zhanqi.tv/games/how",	#2.lushi
	"",					#3.war3	
	"",					#4.baby
        "",    				        #5.WOW
        "",    				        #6.DNF
        "",    				        #7.CF
        "",    				        #8.
	"http://bb.zhanqi.tv/"			#9.
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
	elif link == self.web_urls[5]:
		res = "wow"
	elif link == self.web_urls[6]:
		res = "dnf"
	elif link == self.web_urls[7]:
		res = "cf"
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
