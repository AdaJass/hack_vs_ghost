from ghost import Ghost, Session
from ghost.ghost import TimeoutError
import PySide
import random
import string
from pyquery import PyQuery as pq
import os
import json


agent_list = [
'Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.89 Chrome/62.0.3202.89 Safari/537.36',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'
]

def getip(sip):
    sip.open('http://2017.ip138.com/ic.asp')
    dd=pq(sip.content)
    dd=dd('center').text().split('[')[1].split(']')[0]
    print('my ip is: ', dd)
    return dd
def get_nextip(sip):
    sip.open('http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=&city=0&yys=0&port=11&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=2&regions=')
    d=pq(sip.content)
    # print('getting the ip.',sip.content)
    j=d('body').text()
    j=json.loads(j)
    out = ''
    # print('the ip: ',j)
    if not j.get('success'):
        sip.open('http://web.http.cnapi.cc/index/index/save_white?neek=30958&appkey=32832ae46c07f3e82882c419abcddb66&white='+getip(sip))
        sip.sleep(10)
        out=get_nextip(sip)
    else:
        out=j.get('data')[0]    
    return out

def MakeRequest():        
    gh=Ghost() 
    ran_str2 = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.89 Chrome/62.0.3202.89 Safari/537.36' #.join(random.sample(string.ascii_letters + string.digits, 8)) 
    se=gh.start(display=False)   #Session(gh,user_agent=ran_str2,display=False)  
    sip = gh.start()
    lastnumber=0
    while True:        
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8)) 
        ran_str = ran_str[1:random.randint(1,8)]
        ran_str1 = ''.join(random.sample(string.ascii_letters + string.digits, 8)) 
        ran_str1 = ran_str1[1:random.randint(1,8)]  
        try:
            ip = get_nextip(sip)
            print '\n the new ip is: ',ip
        except Exception:
            pass
        se.set_proxy('https', ip.get('ip'), ip.get('port'))
        agent = agent_list[random.randint(0,4)]
        for x in range(0,15): 
            # print(agent)
            try:
                se.open('https://36kr.com/rank/1',user_agent=agent,timeout=50)
                pass
            except TimeoutError as e:
                print(e,' open error')
                # se.sleep(10)
                continue
                pass
            except Exception:
                pass

            vote_selector = 'li.vote-list-item:nth-child(19) div.support-button'
            # print(se.content)
            # se.show()
            se.sleep(3)
            try:
                se.wait_for_selector(vote_selector,30) 
            except TimeoutError as e:
                print(e)
                continue
                pass
            d=pq(se.content)  
            d=d('li.vote-list-item').eq(18)
            print('here load the page, original tickets is: ', d('span.number').text())
            # se.sleep(1)
            close_selector='div.close-icon'
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
            d=d('li.vote-list-item').eq(18)
            number = d('span.number').text()
            print('after we vote, the ticket is: ',number)
            if lastnumber == number:
                print 'the vote stuck, it will sleep for 15s.'
                se.sleep(15)
            se.click(close_selector,btn=0)            
            se.delete_cookies()
            lastnumber = number 
        se.sleep(random.randint(10,300))           

def main():
    MakeRequest()

if __name__ == '__main__':
    main()
