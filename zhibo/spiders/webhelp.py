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
   #  8.hwzb 
   #  9.sc2
   #  10.movie
   #  11.other
   #
   #
   #
   web_map = {
   'douyu' : [
       "http://www.douyu.com/directory/game/DOTA2",  #0
	"http://www.douyu.com/directory/game/LOL",   #1
	"http://www.douyu.com/directory/game/How",   #2
	"http://www.douyu.com/directory/game/mszb",  #3
	"http://www.douyu.com/directory/game/qmxx",  #4
	"http://www.douyu.com/directory/game/WOW",   #5
	"http://www.douyu.com/directory/game/DNF",   #6
	"http://www.douyu.com/directory/game/CF",    #7
	"http://www.douyu.com/directory/game/yqly",  #8
	"http://www.douyu.com/directory/game/SC",    #9
	"http://www.douyu.com/directory/game/wlrm",  #10
	"http://www.douyu.com/directory/game/TVgame",#11
	"",
	"",
	""
   ],
   'huomao' : [
       "http://www.huomaotv.cn/channel/dota2", #0.doat2
       "http://www.huomaotv.cn/channel/lol",   #1.lol 
       "http://www.huomaotv.cn/channel/ls",    #2.lushi
       "",	                               #3.war3
       "http://www.huomaotv.cn/channel/mnyd",  #4.baby
       "",    				       #5.WOW
       "",    				       #6.DNF
       "",    				       #7.CF
       "",    				       #8.hwzb
       "http://www.huomaotv.cn/channel/sc2",   #9.sc2
       "http://www.huomaotv.cn/live_list?gid=87",#10.movie
       ""                                      #11.other
   ],
   'huya' : [
        "http://www.huya.com/g/dota2",         #0.dota2
	"http://lol.huya.com",                 #1.lol
	"http://www.huya.com/g/393",   	       #2.lushi
	"http://www.huya.com/g/war3",          #3.war3
	"http://www.huya.com/g/1663",          #4.baby
        "http://www.huya.com/g/wow",           #5.WOW
        "http://www.huya.com/g/2", 	       #6.DNF
        "http://www.huya.com/g/cf",    	       #7.CF
        "http://www.huya.com/g/2165",          #8.hwzb
        "",    				       #9.sc2
        "http://www.huya.com/g/2333",          #10.movie
        "http://www.huya.com/g/100002",        #11.other
        "",    				       #12.
        ""				       #13.
    ],
   'panda' : [
       "http://www.panda.tv/cate/dota2",	#0.dota2
	"http://www.panda.tv/cate/lol",         #1.lol
	"http://www.panda.tv/cate/hearthstone", #2.lushi
	"",                                     #3.war3
	"http://www.panda.tv/cate/yzdr", 	#4.baby
        "http://www.panda.tv/cate/wow",   	#5.WOW
        "http://www.panda.tv/cate/dnf",         #6.DNF
        "http://www.panda.tv/cate/cf",    	#7.CF
        "http://www.panda.tv/cate/hwzb",        #8.hwzb
        "http://www.panda.tv/cate/starcraft",   #9.sc2
        "http://www.panda.tv/cate/cartoon",    	#10.movie
	"http://www.panda.tv/cate/zhuji"  	#11other

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
	"http://www.zhanqi.tv/games/war3",	#3.war3	
	"http://bb.zhanqi.tv/",			#4.baby
        "http://www.zhanqi.tv/games/wow",       #5.WOW
        "http://www.zhanqi.tv/games/dnf",       #6.DNF
        "",    				        #7.CF
        "",    				        #8.hwzb
        "",    				        #9.sc2
        "",    				        #10.movie
	"http://www.zhanqi.tv/games/danji",	#11.
	"",
	"",
	"",
	"http://www.zhanqi.tv/games/sanguosha" #san guo sha
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
	elif link == self.web_urls[8]:
		res = "hwzb"
	elif link == self.web_urls[9]:
		res = "sc2"
	elif link == self.web_urls[10]:
		res = "movie"
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
