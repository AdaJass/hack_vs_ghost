from ghost import Ghost, Session
import PySide
import random
import string
from pyquery import PyQuery as pq
import os

agent_list=[
'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)',
'Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)',
'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 ',
'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/19.149.27 Safari/525.13 ',
'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/29.149.27 Safari/525.13 ',
'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/30.149.27 Safari/525.13 ',
'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/39.149.27 Safari/525.13 ',
'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/39.0.27 Safari/525.13 ',
'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/39.222.27 Safari/525.13 ',
'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/40.149.27 Safari/525.13 ',
'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/41.149.27 Safari/525.13 ',
'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
'Opera/10.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
'Opera/10.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
'Opera/11.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
'Opera/11.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
'Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)',
'Mozilla/5.0(compatible;MSIE8.0;WindowsNT5.1)',
'Mozilla/5.0(compatible;MSIE8.0;WindowsNT5.1;Maxthon2.0)',
'Mozilla/5.0(compatible;MSIE8.0;WindowsNT5.1;TencentTraveler5.0)',
'Mozilla/5.0(compatible;MSIE8.0;WindowsNT5.1)',
'Mozilla/5.0(compatible;MSIE8.0;WindowsNT5.1;TheWorld)',
'Mozilla/5.0(compatible;MSIE8.0;WindowsNT5.1;Trident/5.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
'Mozilla/5.0(compatible;MSIE8.0;WindowsNT5.1;360SE)',
'Mozilla/5.0(compatible;MSIE9.0;WindowsNT5.1;AvantBrowser)',
'Mozilla/5.0(compatible;MSIE9.0;WindowsNT5.1)',
'Mozilla/5.0(compatible;MSIE9.0;WindowsNT5.1;Maxthon2.0)',
'Mozilla/5.0(compatible;MSIE9.0;WindowsNT5.1;TencentTraveler5.0)',
'Mozilla/5.0(compatible;MSIE9.0;WindowsNT5.1)',
'Mozilla/5.0(compatible;MSIE9.0;WindowsNT5.1;TheWorld)',
'Mozilla/5.0(compatible;MSIE10.0;WindowsNT5.1;Trident/5.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
'Mozilla/5.0(compatible;MSIE10.0;WindowsNT5.1;360SE)',
'Mozilla/5.0(compatible;MSIE10.0;WindowsNT5.1;AvantBrowser)',
'Mozilla/5.0(compatible;MSIE10.0;WindowsNT5.1)',
'Mozilla/5.0(compatible;MSIE10.0;WindowsNT5.1)',
'Mozilla/5.0(compatible;MSIE10.0;WindowsNT5.1;Maxthon2.0)',
'Mozilla/5.0(compatible;MSIE10.0;WindowsNT5.1;TencentTraveler5.0)',
'Mozilla/5.0(compatible;MSIE11.0;WindowsNT5.1)',
'Mozilla/5.0(compatible;MSIE11.0;WindowsNT5.1;TheWorld)',
'Mozilla/5.0(compatible;MSIE11.0;WindowsNT5.1;Trident/5.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
'Mozilla/5.0(compatible;MSIE11.0;WindowsNT5.1;360SE)',
'Mozilla/5.0(compatible;MSIE11.0;WindowsNT5.1;AvantBrowser)',
'Mozilla/5.0(compatible;MSIE11.0;WindowsNT5.2)',
'Mozilla/5.0(compatible;MSIE12.0;WindowsNT5.1;Maxthon2.0)',
'Mozilla/5.0(compatible;MSIE12.0;WindowsNT5.1;TencentTraveler5.0)',
'Mozilla/5.0(compatible;MSIE12.0;WindowsNT5.1)',
'Mozilla/5.0(compatible;MSIE12.0;WindowsNT5.1;TheWorld)',
'Mozilla/5.0(compatible;MSIE12.0;WindowsNT5.1;Trident/5.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
'Mozilla/5.0(compatible;MSIE12.0;WindowsNT5.1;360SE)',
'Mozilla/5.0(compatible;MSIE12.0;WindowsNT5.1;AvantBrowser)'
# 'Mozilla/5.0(iPhone;U;CPUiPhoneOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5',
# 'Mozilla/5.0(iPod;U;CPUiPhoneOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5',
# 'Mozilla/5.0(iPad;U;CPUOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5',
# 'Mozilla/5.0(Linux;U;Android2.3.7;en-us;NexusOneBuild/FRF91)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1',
# 'MQQBrowser/26Mozilla/5.0(Linux;U;Android2.3.7;zh-cn;MB200Build/GRJ22;CyanogenMod-7)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1',
# 'Opera/9.80(Android2.3.4;Linux;OperaMobi/build-1107180945;U;en-GB)Presto/2.8.149Version/11.10',
# 'Mozilla/5.0(Linux;U;Android3.0;en-us;XoomBuild/HRI39)AppleWebKit/534.13(KHTML,likeGecko)Version/4.0Safari/534.13',
# 'Mozilla/5.0(BlackBerry;U;BlackBerry9800;en)AppleWebKit/534.1+(KHTML,likeGecko)Version/6.0.0.337MobileSafari/534.1+',
# 'Mozilla/5.0(hp-tablet;Linux;hpwOS/3.0.0;U;en-US)AppleWebKit/534.6(KHTML,likeGecko)wOSBrowser/233.70Safari/534.6TouchPad/1.0',
# 'Mozilla/5.0(SymbianOS/9.4;Series60/5.0NokiaN97-1/20.0.019;Profile/MIDP-2.1Configuration/CLDC-1.1)AppleWebKit/525(KHTML,likeGecko)BrowserNG/7.1.18124',
# 'Mozilla/5.0(compatible;MSIE9.0;WindowsPhoneOS7.5;Trident/5.0;IEMobile/9.0;HTC;Titan)',
# 'UCWEB7.0.2.37/28/999',
# 'NOKIA5700/UCWEB7.0.2.37/28/999',
# 'Openwave/UCWEB7.0.2.37/28/999',
# 'Mozilla/4.0(compatible;MSIE6.0;)Opera/UCWEB7.0.2.37/28/999'
]

def MakeRequest():        
    gh=Ghost() 
    ran_str2 = 'User-Agent,Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;' #.join(random.sample(string.ascii_letters + string.digits, 8)) 
    se=Session(gh,user_agent=agent_list[random.randint(0,65)],display=False)  
    lastnumber=0
    while True:
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8)) 
        ran_str = ran_str[1:random.randint(1,8)]
        ran_str1 = ''.join(random.sample(string.ascii_letters + string.digits, 8)) 
        ran_str1 = ran_str1[1:random.randint(1,8)]
        agent = agent_list[random.randint(0,65)]
        print(agent)
        se.open('https://36kr.com/rank/1/option/81',user_agent=agent,timeout=1000)
        vote_selector = 'div.support-button'
        se.wait_for_selector(vote_selector,100)
        close_selector='div.kr-rank-modal-inner div.close-icon'
        for i in range(0,20):
            se.fire('div.kr-rank','scroll')    
        se.scroll_to_anchor('a.footer-logo')        
        se.sleep(3)
        se.fire(vote_selector,'mouseover')  
        se.fire(vote_selector,'mousedown')  
        se.click(vote_selector,btn=0)  
        se.fire(vote_selector,'mouseup')  
        se.fire(vote_selector,'mouseleave')       
        se.sleep(1)
        se.wait_for_selector('div.vote-desc',100)  
        d=pq(se.content) 
        number = d('span.number').text()
        print(number)
        if number == lastnumber:
            se.sleep(random.randint(90,120))
            os.system('python main.py')
            exit()
        # print(se.content) 
        se.click(close_selector,btn=0)
        se.sleep(random.randint(4,5))
        se.delete_cookies()
        lastnumber = number
        # return

def main():
    MakeRequest()

if __name__ == '__main__':
    main()
