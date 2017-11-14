from ghost import Ghost, Session
from ghost.ghost import TimeoutError
import PySide
import random
import string
from pyquery import PyQuery as pq
import os

agent_list=[
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
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

ipdt = [{"ip":"27.220.166.33","port":58878},{"ip":"42.85.4.109","port":2314},{"ip":"106.44.7.153","port":1554},{"ip":"112.248.49.142","port":57856},{"ip":"182.101.41.118","port":3276},{"ip":"123.152.67.31","port":52682},{"ip":"121.233.223.76","port":3278},{"ip":"153.99.184.172","port":51131},{"ip":"121.206.36.109","port":53985},{"ip":"111.177.203.172","port":55374},{"ip":"183.166.230.155","port":3752},{"ip":"124.224.188.133","port":6487},{"ip":"117.92.68.139","port":52444},{"ip":"111.183.229.157","port":57671},{"ip":"125.87.105.120","port":3524},{"ip":"123.156.191.145","port":2156},{"ip":"182.122.34.0","port":57653},{"ip":"36.33.22.118","port":6436},{"ip":"124.224.194.103","port":6487},{"ip":"117.94.71.239","port":53798},{"ip":"42.5.246.77","port":51648},{"ip":"182.244.169.240","port":3429},{"ip":"220.186.188.243","port":3316},{"ip":"117.92.136.79","port":52444},{"ip":"42.5.245.40","port":51648},{"ip":"58.21.186.82","port":2862},{"ip":"58.243.14.44","port":9937},{"ip":"171.42.199.98","port":5374},{"ip":"1.85.73.53","port":2319},{"ip":"111.76.65.238","port":1863},{"ip":"111.79.198.108","port":56214},{"ip":"1.60.63.51","port":56329},{"ip":"117.86.68.31","port":58736},{"ip":"59.63.153.135","port":52455},{"ip":"27.206.176.156","port":58878},{"ip":"222.163.249.117","port":2862},{"ip":"180.109.38.156","port":54813},{"ip":"112.246.35.72","port":58878},{"ip":"182.141.41.132","port":2645},{"ip":"106.56.237.13","port":3245},{"ip":"223.245.208.103","port":52319},{"ip":"124.116.167.197","port":51554},{"ip":"218.67.43.121","port":53985},{"ip":"115.226.135.166","port":2852},{"ip":"101.67.250.207","port":2209},{"ip":"183.143.14.111","port":54252},{"ip":"27.220.123.72","port":58878},{"ip":"111.72.113.145","port":9756},{"ip":"115.219.75.249","port":2316},{"ip":"36.40.201.163","port":1554},{"ip":"124.152.85.17","port":53012},{"ip":"36.33.20.65","port":6436},{"ip":"114.226.132.54","port":59287},{"ip":"122.4.40.125","port":3937},{"ip":"36.33.23.142","port":56436},{"ip":"111.179.89.92","port":57671},{"ip":"111.79.82.177","port":9756},{"ip":"182.38.103.251","port":6605},{"ip":"36.41.111.234","port":52319},{"ip":"114.235.114.245","port":53278},{"ip":"106.46.136.11","port":52847},{"ip":"42.5.244.6","port":51648},{"ip":"111.77.21.83","port":4162},{"ip":"27.157.59.240","port":53985},{"ip":"117.71.155.35","port":52319},{"ip":"122.156.171.133","port":6329},{"ip":"115.213.224.109","port":2852},{"ip":"220.186.135.240","port":52316},{"ip":"49.70.24.131","port":3564},{"ip":"60.168.22.255","port":52644},{"ip":"223.244.35.145","port":53212},{"ip":"202.110.7.33","port":53738},{"ip":"112.122.219.111","port":9937},{"ip":"113.248.83.18","port":5381},{"ip":"123.156.182.236","port":2156},{"ip":"183.142.18.52","port":54252},{"ip":"106.45.178.218","port":2146},{"ip":"36.33.21.191","port":6436},{"ip":"222.208.80.6","port":52645},{"ip":"58.50.228.212","port":5374},{"ip":"123.189.135.101","port":51648},{"ip":"42.87.183.236","port":51648},{"ip":"113.225.70.255","port":55324},{"ip":"223.247.159.163","port":53852},{"ip":"183.143.120.244","port":54252},{"ip":"222.185.211.206","port":59287},{"ip":"117.68.144.169","port":2644},{"ip":"223.247.152.210","port":3852},{"ip":"115.219.73.25","port":52316},{"ip":"122.6.75.206","port":55463},{"ip":"42.52.187.89","port":58943},{"ip":"49.81.90.130","port":53278},{"ip":"112.252.193.87","port":58878},{"ip":"27.157.41.60","port":3985},{"ip":"114.104.230.199","port":53752},{"ip":"119.185.234.170","port":57856},{"ip":"117.94.112.69","port":3798},{"ip":"117.67.130.251","port":52644},{"ip":"36.6.59.83","port":3752},{"ip":"113.143.16.98","port":9020}]

def MakeRequest():        
    gh=Ghost() 
    ran_str2 = 'User-Agent,Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;' #.join(random.sample(string.ascii_letters + string.digits, 8)) 
    se=gh.start()  #Session(gh,user_agent=agent_list[random.randint(0,0)],display=False)     
    lastnumber=0
    for ip in ipdt:
        # ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8)) 
        # ran_str = ran_str[1:random.randint(1,8)]
        # ran_str1 = ''.join(random.sample(string.ascii_letters + string.digits, 8)) 
        # ran_str1 = ran_str1[1:random.randint(1,8)]
        se.set_proxy('https', ip.get('ip'), ip.get('port'))
        for x in xrange(0,3):            
            agent = agent_list[random.randint(0,65)]
            print(agent)
            try:
                se.open('https://36kr.com/rank/1/option/81',user_agent=agent,timeout=50)
                pass
            except TimeoutError as e:
                print(e,' open error')
                se.sleep(10)
                continue
                pass

            vote_selector = 'div.support-button'

            try:
                se.wait_for_selector(vote_selector,10) 
            except TimeoutError as e:
                print(e)
                continue
                pass
            
            close_selector='div.kr-rank-modal-inner div.close-icon'
            for i in range(0,20):
                se.fire('div.kr-rank','scroll')    
            se.scroll_to_anchor('a.footer-logo')        
            se.sleep(2)
            se.fire(vote_selector,'mouseover')  
            se.fire(vote_selector,'mousedown')  
            se.click(vote_selector,btn=0)  
            se.fire(vote_selector,'mouseup')  
            se.fire(vote_selector,'mouseleave')       
            se.sleep(3)
            try:
                se.wait_for_selector('div.vote-desc',10)  
            except TimeoutError as e:
                print(e)
                continue
                pass
            
            d=pq(se.content) 
            number = d('span.number').text()
            print(number)
            # if number == lastnumber:
            #     se.sleep(random.randint(120,180))
            #     os.system('python main.py')
            #     exit()
            # # print(se.content) 
            se.click(close_selector,btn=0)
            se.sleep(random.randint(4,5))
            se.delete_cookies()
            lastnumber = number
            # return

def main():
    MakeRequest()

if __name__ == '__main__':
    main()
