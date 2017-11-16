# -*- coding:utf-8 -*-

from ghost import Ghost, Session

se=Ghost().start(display=False)
se.open('http://www.xfz.cn/explore/2017xfz/?from=timeline&isappinstalled=0#!/topinvestorunder30/1',\
    user_agent= 'Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255')
se.sleep(10)
se.delete_cookies()
se.click('div.vote-button')
# print(se.content)
# se.exit()
exit()
    
